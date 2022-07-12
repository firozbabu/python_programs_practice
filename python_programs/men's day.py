def H():
    for i in range(6):
        for h in range(5):
            if (i == 2):
                print("M", end='')
            else:
                if (h == 0 or h == 4):
                    print("M", end='')
                else:
                    print(end=' ')
        print()
                
H()
