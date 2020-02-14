class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, data):
        if self.val == data:
            return False
        elif self.val > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self,data):
        if self.val == data:
            return True
        elif self.val > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.val))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.val))

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.val))
            if self.right:
                self.right.inorder()
        
            
class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)

    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print('PreOrder')
        self.root.preorder()

    def postorder(self):
        print('PostOrder')
        self.root.postorder()

    def inorder(self):
        print('InOrder')
        self.root.inorder()

        
l=list(map(int,input().split()))
bst=Tree()
for i in l:
    bst.insert(i)
bst.postorder()
