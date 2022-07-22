
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return '->'.join(nodes)

llist = LinkedList()
print(llist)


first_node = Node('a')
llist.head = first_node
print(llist)

second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node
print(llist)

'''






'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None



    def __repr__(self):

        node = self.head
        nodes = []
        while node :
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return '->'.join(nodes)



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

List = LinkedList()
List.head = a
a.next = b
b.next = c
c.next = d
print(List)
'''



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class Single:

    def __init__(self):
        self.head = None

    def addnode(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = node

    def display(self):
        nodes = []
        if self.head!=None:
            temp = self.head
            while temp!=None:
                nodes.append(temp.data)
                temp=temp.next
            print(*nodes,sep=' -> ')
        else:
            print('Linked list is empty')

    def get_middle_element(self):

        fast_pointer = self.head
        slow_pointer = self.head
        while fast_pointer.next and fast_pointer.next.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        return slow_pointer.data


    def reverse(self):

        current_node = self.head
        previous_node = None
        next_node = None

        while current_node:

            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node



    

sll = Single()
for i in [1,2,3,4,5,6,7,8,9,5,3,6,2,7,8,2,3,5,6,9,9,1,4,0]:
    sll.addnode(i)
sll.display()
print(sll.get_middle_element())
sll.reverse()
sll.display()
