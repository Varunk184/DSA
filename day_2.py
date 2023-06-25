class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left =Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
        
    def printt(self):
        if self.left:
            self.left.printt()
        print(self.data)
        if self.right:
            self.right.printt()
    


    def inOrder(self,root):
        res=[]
        if root:
            res=self.inOrder(root.left)
            res.append(root.data)
            res=res+self.inOrder(root.right)
        return res
    
    def preOrder(self,root):
        res=[]
        if root:
            res.append(root.data)
            res=res+self.preOrder(root.left)
            res=res+self.preOrder(root.right)
        return res
    def postOrder(self,root):
        res=[]
        if root:
            res=self.postOrder(root.left)
            res=res+self.postOrder(root.right)
            res.append(root.data)
        return res
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(28)
root.printt()
print(root.inOrder(root))
print(root.preOrder(root))
print(root.postOrder(root)) 