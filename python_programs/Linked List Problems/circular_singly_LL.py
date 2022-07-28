class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class CircularSingle:

    def __init__(self):
        self.head = None
        self.tail  = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def Circular(self,nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node

c = CircularSingle()
c.Circular(5)
c.Circular(10)
print([node.value for node in c])
