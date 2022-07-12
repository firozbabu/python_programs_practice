import time
import os
os.system('call')

def A():
    for a in range(6):
        if (i == 0 or i == 3):
            print("\u001b[47m\u001b[35m*\u001b[0m", end='')
        else:
            if (a == 0 or a == 5):
                print("\u001b[47m\u001b[35m*\u001b[0m", end='')
            else:
                print(end=' ')


def H():
    for h in range(5):
        if (i == 2):
            print("\u001b[41m\u001b[33m*\u001b[0m", end='')
        else:
            if (h == 0 or h == 4):
                print("\u001b[41m\u001b[33m*\u001b[0m", end='')
            else:
                print(end=' ')



def P():
    for p in range(5):
        if (i == 0 or i == 3):
            if (p == 4):
                print('\u001b[43m \u001b[0m',end='')
            else:
                print("\u001b[43m\u001b[32;1m*\u001b[0m", end='')
        elif (i == 1 or i == 2):
            if (p == 0 or p == 4):
                print("\u001b[43m\u001b[32;1m*\u001b[0m", end='')
            else:
                print(end=' ')
        elif (i == 4 or i == 5):
            if (p == 0):
                print("\u001b[43m\u001b[32;1m*\u001b[0m", end='')
            else:
                print(end=' ')


def P1():
    for p in range(5):
        if (i == 0 or i == 3):
            if (p == 4):
                print('\u001b[45m \u001b[0m',end='')
            else:
                print("\u001b[45m\u001b[38m*\u001b[0m", end='')
        elif (i == 1 or i == 2):
            if (p == 0 or p == 4):
                print("\u001b[45m\u001b[38m*\u001b[0m", end='')
            else:
                print(end=' ')
        elif (i == 4 or i == 5):
            if (p == 0):
                print("\u001b[45m\u001b[38m*\u001b[0m", end='')
            else:
                print(end=' ')


def Y():
    for y in range(5):
        if (i == 0):
            if (y == 0 or y == 4):
                print("\u001b[46m*\u001b[0m", end='')
            else:
                print(end=' ')
        elif (i == 1):
            if (y == 1 or y == 3):
                print("\u001b[46m*\u001b[0m", end='')
            else:
                print(end=' ')
        elif (i == 2 or i == 3 or i == 4 or i == 5):
            if (y == 2):
                print("\u001b[46m*\u001b[0m", end='')
            else:
                print(end=' ')



def M():
    for m in range(7):
        if (i == 1):
            if (m == 2 or m == 3 or m == 4):
                print(end=' ')
            else:
                print("\u001b[47m\u001b[30m*\u001b[0m", end='')
        elif (i == 2):
            if (m == 1 or m == 3 or m == 5):
                print(end=' ')
            else:
                print("\u001b[47m\u001b[30m*\u001b[0m", end='')
        elif (i == 3):
            if (m == 0 or m == 3 or m == 6):
                print("\u001b[47m\u001b[30m*\u001b[0m", end='')
            else:
                print(end=' ')
        else:
            if (m == 0 or m == 6):
                print("\u001b[47m\u001b[30m*\u001b[0m", end='')
            else:
                print(end=' ')


def N():
    for n in range(7):
        if (i == 1):
            if (n == 2 or n == 3 or n == 4 or n == 5):
                print(end=' ')
            else:
                print("\u001b[45m\u001b[36;1m*\u001b[0m",end='')
        elif (i == 2):
            if (n == 1 or n == 3 or n == 4 or n == 5):
                print(end=' ')
            else:
                print("\u001b[45m\u001b[36;1m*\u001b[0m",end='')
        elif (i == 3):
            if (n == 0 or n == 3 or n == 6):
                print("\u001b[45m\u001b[32;1m*\u001b[0m",end='')
            else:
                print(end=' ')
        elif (i == 4):
            if (n == 0 or n == 5 or n == 6):
                print("\u001b[45m\u001b[32;1m*\u001b[0m",end='')
            else:
                print(end=' ')
        else:
            if (n == 0 or n == 6):
                print("\u001b[45m\u001b[32;1m*\u001b[0m",end='')
            else:
                print(end=' ')

def D():
    for d in range(6):
        if (i == 0 or i == 5):
            if (d == 5):
                print(end=' ')
            else:
                print("\u001b[41m*\u001b[0m", end='')
        elif (i == 1 or i == 2 or i == 3 or i == 4):
            if (d == 0 or d == 5):
                print("\u001b[41m*\u001b[0m", end='')
            else:
                print(end=' ')


def E():
    for e in range(5):
        if (i == 0 or i == 2 or i == 5):
            print("\u001b[43m\u001b[35;1m*\u001b[0m",end='')
        else:
            if (e == 0):
                print("\u001b[43m\u001b[35;1m*\u001b[0m",end='')
            else:
                print(end=' ')

def S():
    for s in range(5):
        if (i == 0 or i==2 or i==5):
            print("\u001b[42m\u001b[33m*\u001b[0m",end='')
        elif(i == 1):
            if (s == 0):
                print("\u001b[42m\u001b[33m*\u001b[0m",end='')
            else:
                print(end=' ')
        elif (i == 3 or i == 4):
            if (s == 4):
                print("\u001b[42m\u001b[33m*\u001b[0m",end='')
            else:
                print(end=' ')

print('\n\n\n\n\n\n\n\n\n\n\n                                           =============================xxxxxxxxxxxxxxxxxxxxx============================\n\n\n\n\n\n\n\n')

for i in range(6):
    time.sleep(1)
    print(end='                                         ')
    H()
    print(end=' ')
    A()
    print(end=' ')
    P()
    print(end=' ')
    P1()
    print(end=' ')
    Y()
    print(end='   ')
    M()
    print(end=' ')
    E()
    print(end=' ')
    N()
    print(end=' ')
    if i==0:
        print('\u001b[47m \u001b[0m',end='')
    else:
        print(end=' ')
    print(end=' ')
    S()
    print(end='   ')
    D()
    print(end=' ')
    A()
    print(end=' ')
    Y()
    print()
print('\n',
    end='                                                                                      \u001b[43m ---> Art By MEME PROGRAMMERS TELUGU \u001b[0m')
print('\n\n\n\n\n\n\n\n                                           =============================xxxxxxxxxxxxxxxxxxxxx============================\n\n\n')
print('\n\n\n\n\n\n\n\n\n')
