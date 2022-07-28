
'''

class Node:

    def __init__(self,data,next=None):

        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):

        self.head=None


    def insert(self,data):
        newnode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
        else:
            self.head = newnode


    def printl(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

            
l = LinkedList()
l.insert(3)
l.insert(4)
l.insert(5)
l.printl()
'''
class Node:

    def __init__(self,val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self,val):
        self.val = val


    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next


        

class LinkedList:

    def __init__(self,head=None):
        self.head = head
        self.count = 0

    def insert(self,data):



        #create a new node to hold the data
        new_node = Node(data)
        
        #set the next of the new node to the current node
        new_node.set_next(self.head)
        
         #set the head of the linked list to the new head
        self.head = new_node
        self.count +=1


    def find(self,val):

        #start with first item in linked list
        item = self.head


        #itrerate over the next nodes
        #but if item!=None the end search
        while item!=None:


            #if the data in item matched val then return item
            if item.get_data() == val:
                return item

            #otherwise we get next item in list
            else:
                item = item.get_next()

                
        #if while loop breaks with None then nothing found
        #so we return None
        return None




    def remove(self,item):

        #set the current node starting with the head
        current = self.head

        #create a previous node to hold the one before
        #the node we want to remove
        previous = None

        #while current is note None then we can search for it

        while current is not None:
            if current.data == item:
                break

            #otherwise we set previous to current and current to the next
            #item in list

            previous = current
            current = current.get_next()


        #if the current is None then item not in the list
        if current is None:
            raise ValueError(f'{item} is not in the list')
        #if previous None then the item is at the head
        if previous is None:
            self.head = current.head
            self.count -=1

        else:
            #otherwise then we remove that node from the list
            previous.set_next(current.get_next())
            self.count -=1

    def get_count(self):

        return self.count

    def is_empty(self):

        return self.head == None


    def printl(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

            

l = LinkedList()
l.insert(5)
l.insert(4)
l.insert(3)
l.insert(0)
l.insert(1)
l.printl()
print(l.get_count())
print(l.is_empty())








