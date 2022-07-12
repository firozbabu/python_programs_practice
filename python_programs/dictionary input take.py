Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l = []
>>> for i in range(3):
	l.append((int,input()))

	
3 6

4 5
>>> l
[(<class 'int'>, '3 6'), (<class 'int'>, ''), (<class 'int'>, '4 5')]
>>> l = []
>>> for i in range(3):
	l.append((int(input()),input()))

	
3 4
Traceback (most recent call last):
  File "<pyshell#7>", line 2, in <module>
    l.append((int(input()),input()))
ValueError: invalid literal for int() with base 10: '3 4'
>>> p = ((int(input()),input()) for i in range(3))
>>> p
<generator object <genexpr> at 0x000001F422B1B430>
>>> p= [(int(input()),input()) for i in range(3)]
5 6
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    p= [(int(input()),input()) for i in range(3)]
  File "<pyshell#10>", line 1, in <listcomp>
    p= [(int(input()),input()) for i in range(3)]
ValueError: invalid literal for int() with base 10: '5 6'
>>> p = [(int(input()),input()) for i in range(3)]
5 6
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    p = [(int(input()),input()) for i in range(3)]
  File "<pyshell#11>", line 1, in <listcomp>
    p = [(int(input()),input()) for i in range(3)]
ValueError: invalid literal for int() with base 10: '5 6'
>>> p = [(int(input()),input()) for i in range(3)]
4
5
3
4
5
1
>>> p
[(4, '5'), (3, '4'), (5, '1')]
>>> p = [(int(input('Key:')),input('Value:')) for i in range(3)]
Key:4
Value:54
Key:0
Value:12
Key:12
Value:3
>>> p
[(4, '54'), (0, '12'), (12, '3')]
>>> dict(p)
{4: '54', 0: '12', 12: '3'}
>>> p = dict((int(input('Key:')),input('Value:')) for i in range(3))
Key:6
Value:5
Key:3
Value:3
Key:5
Value:6
>>> p
{6: '5', 3: '3', 5: '6'}
>>> 