from operations import *

a = float(input('Enter Number 1: '))
b = float(input('Enter Number 2: '))
option = int(input('Enter 1 for Addition or Enter 2 for Subtraction or Enter 3 for multiplication or Enter 4 for Division: '))
if option == 1:
    print(addition(a,b))
elif option == 2:
    print(subtraction(a,b))
elif option == 3:
    print(multiplication(a,b))
elif option == 4:
    print(division(a,b))
else:
    print('you have chosen wrong option')
