class Node:
    def __init__(self,value=None):

        self.value = value
        self.prev = None
        self.next = None

class Doubly:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):

        node = self.head

        while node:
            yield node
            node= node.next


    def doubly(self,nodeval):
        node = Node(nodeval)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "success"


    def deleteDll(self):
        if self.head is None:
            print('no elements in the DLL')

        else:

            tempnode = self.head

            while tempnode:
                tempnode.prev = None
                tempnode = tempnode.next

            self.head  = None
            self.tail = None
            print("dll is deleted")


    def insert(self,value,location):

        if self.head is None:
            print('No insertion is done')
        else:
            newnode = Node(value)
            if location == 0:

                newnode.prev = None
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode

            elif location==1:

                newnode.next = None
                newnode.prev=self.tail
                self.tail.next = newnode
                self.tail = newnode

            else:

                tempnode = self.head
                index = 0
                while index<location-1:
                    tempnode = tempnode.next
                    index+=1
                newnode.next = tempnode.next
                newnode.prev = tempnode
                newnode.next.prev = newnode
                tempnode.next = newnode


    def traverse(self):
        if self.head is None:
            print('no elements in ll')
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next

    def reverse(self):

        if self.head is None:
            print('no elements')
        else:
            tempnode = self.tail
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.prev


    def search(self,nodevalue):

        if self.head is None:
            return 'no elements are there'

        else:
            tempnode = self.head
            count = 0
            while tempnode:
                if tempnode.value == nodevalue:
                    return f'match found at {count} index'
                tempnode = tempnode.next
                count+=1
            return 'no match found in the ll'

    def delete(self,location):

        if self.head is None:
            return 'no elements'

        else:

            if location==0:

                if self.head == self.tail:

                    self.head = None
                    self.tail  = None
                else:
                    self.head = self.head.next
                    self.head.prev = None

            elif location == 1:

                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:

                tempnode  = self.head
                index = 0
                while index<location-1:

                    tempnode = tempnode.next
                    index+=1
                tempnode.next = tempnode.next.next
                tempnode.next.prev = tempnode
                
                
                
t = Doubly()
t.doubly(5)
print([i.value for i in t])
t.insert(6,1)
print([i.value for i in t])
t.insert(100,0)
print([i.value for i in t])
t.insert(23,2)
print([i.value for i in t])

t.traverse()

t.reverse()
print(t.search(23))

t.delete(1)
print([i.value for i in t])
t.delete(1)
print([i.value for i in t])
t.deleteDll()
t.delete(1)
print([i.value for i in t])
