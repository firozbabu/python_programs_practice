class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def inorder(self,root):
        output = []

        if root:

            output = self.inorder(root.left)
            output.append(root.data)
            output = output+self.inorder(root.right)

        return output


    def postorder(self,root):

        output = []
        if root:

            output = self.postorder(root.left)
            output = output+self.postorder(root.right)
            output.append(root.data)
        return output
    def preorder(self,root):

        output = []
        if root:
            output.append(root.data)
            output = output+self.preorder(root.left)
            output = output+self.preorder(root.right)

        return output




data = [13,5,23,4,6,22,28,3,3,27,32]
root = Node(data.pop(0))

for d in data:
    root.insert(d)

print('inorder   ',root.inorder(root))
print('postorder   ',root.postorder(root))
print('preorder    ',root.preorder(root))
