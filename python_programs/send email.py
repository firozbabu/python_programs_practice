import smtplib

from fileinput import filename
from bs4 import BeautifulSoup
import requests
import pandas as pd
import win32com.client as win32
from string import ascii_lowercase
from random import choices
title = 'plumber'
location = 'India'
address =[]
page=1
while page!=3:
        url = f'https://www.yellowpages.ca/search/si/{page}/{title}/{location}'
        html_page = requests.get(url)
        soup = BeautifulSoup(html_page.content, 'html.parser')
        block = soup.findAll('div',class_='listing__content__wrap--flexed jsGoToMp')
        for i in block:
            r = i.find('a',class_='listing__name--link listing__link jsListingName')
            if i.find('span',class_='listing__address--full'):
                add = i.find('span',class_='listing__address--full')
                a = ' '.join([j.text for j in add.findAll('span',class_='jsMapBubbleAddress')]) 
            else:
                a=None
            if i.find('a',class_='mlr__item__cta jsMlrMenu'):
                phon = i.find('ul',class_='mlr__submenu')
                phon = phon.find('h4').text
            
            else:
                phon = None
            address.append((r.text,a,phon))
        page+=1
print('extracted')
print('now creating excel file')
df = pd.DataFrame(address, columns=['Name of the profession ', 'Address', 'Phonenumber'])
lowercase = ascii_lowercase
file_name = ''.join(choices(lowercase,k=6))+'.xlsx'
df.to_excel(file_name)
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(r'C:\Users\shaik firoz babu\Documents\scrapy_bs4\\'+str(file_name))
ws = wb.Worksheets("Sheet1")
ws.Columns.AutoFit()
wb.Save()
excel.Application.Quit()










import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = '''Here is your scrapped file content'''
sender_address = 'captainfiroz1@gmail.com'
sender_pass = '4FMhsp90'
receiver_address = 'bellammanikanta506@gmail.com'
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Excel file content with scrapped data'
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = file_name
attach_file = open(attach_file_name, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) 
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
