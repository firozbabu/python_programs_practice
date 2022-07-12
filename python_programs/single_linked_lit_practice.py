"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def create_linked_list(self,value):
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
        val = self.head
        while val !=None:
            nodes.append(val.data)
            val = val.next
        return nodes

l = LinkedList()
for i in [6,3,0,1,5,3,5,6,3,2,4,91,45]:
    l.create_linked_list(i)
print(* l.display(),sep=' -> ')
"""

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def create_linked(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node

        else:

            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next=node


    def __iter__(self):
        item = self.head
        while item!=None:
            yield item.data
            item = item.next


    def insert_at_head(self,value):
        node = Node(value)
        node.next= self.head
        self.head = node

    def insert_at_end(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = node



    def search(self,value):
        count = 0
        if self.head==None:
            return 'linked list does not exist'

        else:
            temp = self.head
            while temp is not None:
                if temp.data==value:
                    return f'element found at {count-1} index and {count} position'
                count+=1
                temp = temp.next
            return f'element {value } not found'


    def delete_head(self):
        if self.head==None:
            return
        else:
            tempnode = self.head
            self.head = self.head.next
            tempnode = None

    def delete_tail(self):

        temp = self.head
        while temp.next!=None:
            prev = temp
            temp = temp.next

        prev.next = None



    def delete_linkedlist(self):
        if self.head is  None:
            return 'linked list is not existed'
        self.head = None
        return 'deleted_single_linked list'
d = LinkedList()
for i in [7,42,0,1,4,51,5,4,1,4,1,0,6,7,9]:
    d.create_linked(i)

d.insert_at_head(30030303)

d.insert_at_end(45545454545454545)

print(d.search(1000))
print(*[i for  i in d],sep=' -> ')
d.delete_tail()
#for i in range(3):
 #   d.delete_head()

print(d.delete_linkedlist())
print(*[i for  i in d],sep=' -> ')
            




