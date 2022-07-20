class Node:
    def __init__(self,value= None):

        self.value = value
        self.prev = None
        self.next = None


class circular:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):

        node = self.head

        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create(self,nodevalue):

        newnode = Node(nodevalue)
        self.head = newnode
        self.tail = newnode
        newnode.prev = newnode
        newnode.next = newnode


    def insert(self,value,location):

        if self.head is None:
            return 'No elements'

        else:
            newnode = Node(value)
            if location==0:

                newnode.next = self.head
                newnode.prev = self.tail
                self.head.prev = newnode
                self.head = newnode
                self.tail.next  = newnode

            elif location == 1:
                newnode.next = self.head
                newnode.prev = self.tail
                self.head.prev = newnode
                self.tail.next  = newnode
                self.tail = newnode

            else:
                index = 0
                tempnode = self.head
                while index<location-1:
                    tempnode = tempnode.next
                    index+=1
                newnode.next = tempnode.next
                newnode.prev = tempnode
                newnode.next.prev = newnode
                tempnode.next = newnode

    def traverse(self):
        if self.head is None:
            return "no elements"
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value,end=' ')
                if tempnode == self.tail:
                    break
                tempnode = tempnode.next

    def reversetraverse(self):

        if self.head is None:
            print('no elements')

        else:

            tempnode = self.tail
            while tempnode:
                print(tempnode.value,end=' ')
                if tempnode == self.head:
                    break
                tempnode = tempnode.prev


    def search(self,nodevalue):
        if self.head is None:
            print('No element')

        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == nodevalue:
                    return tempnode.value
                if tempnode == self.tail:
                    return 'value does not exist'

                tempnode = tempnode.next
    def delete(self,location):
        if self.head is None:
            return 'no elements'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.tail = None
                    self.head = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head


            elif location==1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.tail = None
                    self.head = None

                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail

            else:
                currnode = self.head
                index = 0
                while index<location-1:
                    currnode = currnode.next
                    index+=1
                currnode.next = currnode.next.next
                currnode.next.prev = currnode
                
    def deleteCDLL(self):

        if self.head is None:
            return 'No elements'

        else:

            self.tail.next= None
            tempnode = self.head
            while tempnode:
                tempnode.prev = None
                tempnode = tempnode.next

            self.head = None
            self.tail = None
            
cir = circular()
cir.create(5)
print([[i.value] for i in cir])
cir.insert(100,0)
print([[i.value] for i in cir])
cir.insert(10000,1)
print([[i.value] for i in cir])
cir.insert(434343,2)
print([[i.value] for i in cir])
#cir.traverse()
#cir.reversetraverse()
#print(cir.search(0))
cir.deleteCDLL()
print([[i.value] for i in cir])
