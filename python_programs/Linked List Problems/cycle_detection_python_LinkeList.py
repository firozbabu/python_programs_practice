class Node:

    def __init__(self,value,next_node=None):

        self.value = value
        self.next = next_node

    def has_cycle(self,head):
        slow,fast = head,head
        while fast  and fast.next:
            slow,fast = slow.next,fast.next.next
            if slow == fast:
                return True
        return False


node4 = Node(4)
ll = Node(1,Node(2,Node(3,node4)))
node4.next = ll
print(ll.has_cycle(ll))
