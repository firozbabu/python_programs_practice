class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        temp = self.head
        t = ''
        while temp:
            t+=str(temp.data)+' = > '
            temp= temp.next
        t+='None'
        print(t)


    def insertion(self,pos,val):

        target = Node(val)

        if pos ==0:
            target.next = self.head
            self.head = target
            return

        def getpos(pos):
            temp = self.head
            count=1
            while count<pos:
                temp = temp.next
                count+=1

            return temp
        prev = getpos(pos)
        nextnode = prev.next
        prev.next = target
        target.next = nextnode

    def delete(self,key):

        if self.head is None:
            return

        temp = self.head
        if temp.data == key:
            self.head = temp.next
            temp = None
            return
        while temp.next.data != key:
            temp = temp.next

        target = temp.next
        temp.next = target.next
        target.next = None
        

LL = LinkedList()
LL.head = Node(4)
second = Node(5)
third = Node(3)
fourth = Node(1)


LL.head.next = second
second.next = third
third.next = fourth

LL.insertion(0,454)
LL.insertion(0,454)
LL.insertion(2,111)
LL.delete(111)
LL.printLL()
LL.delete(4)
LL.printLL()        
