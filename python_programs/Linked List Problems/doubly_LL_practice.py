class Node:

    def __init__(self,data):
        self.data = data
        self.next = None



class Linked:

    def __init__(self):
        self.head = None

    def create(self,arr):

        start = self.head
        n = len(arr)
        temp = start
        i =0
        while i<n:
            newnode = Node(arr[i])
            if i==0:
                start = newnode
                temp = start

            else:
                temp.next = newnode
                newnode.prev = temp
                temp = temp.next
            i+=1

        self.head = start
        return start
    def print(self):
        temp = self.head
        linked =''
        while temp:
            linked+=str(temp.data)+' => '
            temp = temp.next
        linked+='None'

        print(linked)

    def countlist(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count+=1
        return count

    def insert(self,value,index):
        temp = self.head
        count = self.countlist()

        if count+1 < index:
            return temp
        newnode = Node(value)
        if index ==1:
            newnode.next = temp
            temp.prev = newnode
            self.head = newnode

        if (index==count+1):
            while ( temp.next is not None):
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp

        i=1
        while (i<index-1):
            temp = temp.next
            i+=1

        newtarget = temp.next
        
        newnode.next = newtarget
        newtarget.prev = newnode
        
        temp.next = newnode
        newnode.prev = temp
    def deletion(self,index):
        temp = self.head
        count = self.countlist()
        if count<index:
            return temp
        if index == 1:
            temp = temp.next
            self.head = temp

        if count == index:
            while temp is not None and temp.next.next is not None:
                temp = temp.next
            temp.next  = None

        i  = 1
        while i<index-1:
            temp = temp.next
            i+=1

        prevnode = temp
        nodetarget = temp.next
        nextnode = nodetarget.next
        nextnode.prev = prevnode
        prevnode.next = nextnode
        
        
L = Linked()
L.create([3,1,5,6,2,7,0])
L.insert(10000,1)
L.insert(5454545,4)
L.print()
L.deletion(4)
L.print()
