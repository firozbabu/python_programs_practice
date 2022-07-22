

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):

        node = self.head
        while node:
            yield node
            node = node.next

    def print_ll(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def insertstart(self,val):
        node = Node(val)
        node.next = self.head
        self.head = node


    def insertend(self,val):
        node = Node(val)
        nodehead = self.head
        while nodehead.next:
            nodehead= nodehead.next
        nodehead.next = node

    def insert_Between_nodes(self,targetnode,newnode):
        node = self.head
        new = Node(newnode)
        while node:
            if targetnode == node.data:
                next_node = node.next
                node.next = new
                new.next = next_node
                return
            node = node.next

    def remove_head(self):
        self.head = self.head.next 




obj = LinkedList()
node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')
obj.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

'''
print([i.data for i in obj])
obj.insertstart(1000)
print([i.data for i in obj])
obj.insertstart(9)
print([i.data for i in obj])
obj.insertstart(99)
print([i.data for i in obj])
obj.insertend(2345)
print([i.data for i in obj])
obj.insertend('ABC')
print([i.data for i in obj])
obj.insert_Between_nodes('E','EF')
print([i.data for i in obj])
obj.remove_head()
print([i.data for i in obj])
obj.remove_head()
print([i.data for i in obj])
obj.remove_head()
print([i.data for i in obj])
obj.remove_head()
print([i.data for i in obj])
'''
'''
st = ''
head = obj.head
while head:
    st +=head.data
    st+=' - > '
    head = head.next

st+='None'
print(st)
'''
#print(obj.print_ll())
