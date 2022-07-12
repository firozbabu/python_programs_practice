class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class single:
    def __init__(self):
        self.head = None


    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

            
    def createLinkedList(self,value):
        newnode = Node(value)
        if self.head==None:
            self.head = newnode
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = newnode

    def insert_at_start(self,value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode
s = single()
for i in [1,2,3,4,5,6,7,8,9,9]:
    s.createLinkedList(i)

s.insert_at_start(21)
s.insert_at_start(31)
print([node.data for node  in s])
