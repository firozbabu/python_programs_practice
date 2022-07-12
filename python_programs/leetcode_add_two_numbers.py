list1=int(''.join(reversed(list(map(str,input().split())))))
list2=int(''.join(reversed(list(map(str,input().split())))))
res=str(list1+list2)
print(list(map(int,reversed(res))))

