

'''
count=0
for i in string:
    count+=1
print(count)
'''
'''
d = {}
for i in string:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''
'''
if len(string)<2:
    print('Empty String')

else:
    print(string[:2]+string[len(string):-3:-1])
'''

'''
print(string[0]+string[1:].replace(string[0],'$'))
'''
'''
string1 = list(string1)
string2 = list(string2)
string1[:2],string2[:2]=string2[:2],string1[:2]
print(''.join(string1)+' '+''.join(string2))
'''

'''
if len(string)<3:
    print(string)
elif string.endswith('ing'):
    string+='ly'
elif not string.endswith('ing'):
    string+='ing'
print(string)
'''

'''
print(max(string,key = len))
'''

'''
ind = int(input())
print(string.replace(string[ind],''))
'''


'''
print(string[-1]+string[1:-1]+string[0])
'''


'''
poor = string.find('poor')
n = string.find('not')
if n<poor and n>0 and poor>0:
    print(string.replace(string[n:poor+4],'good'))
else:
    print(string)
'''
'''
string = input()
print(string[::2])
'''
'''
string = input().split()
d = {}
for i in string:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''
'''
string = input().split()
print(' '.join(i.lower() for i in string))
'''
'''
string = input().split(',')
print(','.join(sorted(set(string))))
'''
'''
def f(tag,string):
    return f'<{tag}>{string}</{tag}>'
tag = input()
string = input()
print(f(tag,string))
'''
'''
string = input()
print(string[len(string)-2:]*4)
'''
'''
string = input()
print(string[:3] if len(string)>3 else string)
'''

'''
def f(char,string):
    return string.rsplit(char,1)[0]
char = input()
string = input()
print(f(char,string))
'''

'''
string = input()
print(string[::-1] if len(string)%4==0 else string)
'''
'''
number = float(input())
print(f'{round(number,2):.2f}')
print(f'{number:.2f}')
'''
'''
import textwrap
sample_text =''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    ''
text1 = textwrap.dedent(sample_text)
print(textwrap.fill(text1,initial_indent='',subsequent_indent=' '*4,width=80))
'''
'''
def f(string):
    count = 0
    for i in range(4):
        if string[i].isupper():
            count+=1
    if count>=2:
        return string.upper()
    else:
        return string
print(f('PyThon'))
'''
'''
string = input()
print(''.join(sorted(string)))
'''

'''
string = input()
string = string.strip()
print(string)
'''
'''
string = input()
s = input()
print(string.startswith(s))
'''
from string import ascii_lowercase
s = ascii_lowercase
sr = input().lower()
shift = int(input())
str =''
for i in range(len(sr)):
    print(s[(s.index(sr[i])+shift)%26])
    print((s.index(sr[i])+shift)%26)













    







































