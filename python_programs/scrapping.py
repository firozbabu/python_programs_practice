import requests
from bs4 import BeautifulSoup
result = requests.get("https://devpost.com/hackathons?utf8=%E2%9C%93&search=blockchain&challenge_type=all&sort_by=Submission+Deadline")
src = result.content
soup = BeautifulSoup(src, 'lxml')
names =soup.find_all('div',class_='eachPopular')
for name in names:
    n = name.find('a').get_text()
    print(n)
