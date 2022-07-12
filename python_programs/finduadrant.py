x = int(input())
y = int(input())

if x>0 and y>0:
    print('Ist quadrant')
elif x<0 and y>0:
    print('II nd quadrant')
elif x<0 and y<0:
    print('IIIrd quadrant')
elif x>0 and y<0:
    print('IVth quadrant')
else:
    print('ORIGIN')
