class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Single:
    def __init__(self):
        self.head = None
        self.tail = None
    def create_SLL(self,value):
        node = Node(value)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next



    #linked list methods implementation

    # to check if the linked list is empty or not
    def isempty(self):
        if self.head == None and self.tail == None:
            return True
        else:
            return False

    #add element to first
    def addToStart(self,value):
        node = Node(value)
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node


    #add element to the last
    def addToEnd(self,value):
        node = Node(value)
        if self.head == None and self.tail==None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    #display the linked list
    def display(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append(None)
        print(*nodes,sep=' -> ')

    #length of the linked list
    def length(self):
        count=0
        node = self.head
        while node:
            node=node.next
            count+=1
        return count


    #count() method implementation element occurences
    def count(self):
        d = {}
        node = self.head
        while node:
            if node.data in d:
                d[node.data]+=1
            else:
                d[node.data]=1
            node = node.next
        return d

    #finding maximum element
    def find_max(self):
        m = self.head
        node = self.head
        while node:
            if m.data<node.data:
                m=node
            node = node.next
        return m.data

    #finding minimum element

    def find_min(self):
        m = self.head
        node = self.head
        while node:
            if m.data > node.data:
                m= node
            node = node.next
        return m.data

    #clear method implementation to clear the linked list

    def clear(self):
        self.head = None
        self.tail = None
        

            
c = Single()

#print(c.isempty()) -> False

c.create_SLL(10)
arr = [4,5,2,8,9,1,0,200,-22]
for i in arr:
    c.create_SLL(i)

#print(c.tail.data)
#print(*[i.data for i in c],sep=' -> ')

#print(c.isempty()) -> True

#c.addToStart(-1)
#print(*[i.data for i in c],sep=' -> ')
#c.addToStart(-22)
#print(*[i.data for i in c],sep=' -> ')

#c.addToEnd(-1)
#print(*[i.data for i in c],sep=' -> ')
#c.addToEnd(-22)
#print(*[i.data for i in c],sep=' -> ')

#c.display()
#print(c.length())
#print(c.count())
#print(c.find_max())
#print(c.find_min())
c.clear()

c.display()
