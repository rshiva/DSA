# node -> value, left, right
# BST --> root/head
#insert -> root, data
#search -> data
#inorder ->  left, root, right
#preorder -> root, left ,right
#postorder -> lef, right, root

class Node():
  def __init__(self,value):
    self.left = None
    self.right = None
    self.value = value


class BST():
  def __init__(self):
    self.root = None


  def insert(self,root, value):
    if root ==  None:
      root = Node(value)
    elif value <= root.value:
      if root.left is None:
        root.left = Node(value)
      else:
        root.left = self.insert(root.left, value)
    elif value >= root.value:
        if root.right is None:
          root.right = Node(value)
        else:
          root.right = self.insert(root.right, value)
    return root

  def inorder(self, root): 
    if root: 
        self.inorder(root.left) 
        print(root.value) 
        self.inorder(root.right) 
  
  def preorder(self, root): 
    if root: 
      print(root.value) 
      self.preorder(root.left)
      self.preorder(root.right) 
    

  def postorder(self, root): 
    if root: 
      self.postorder(root.left)
      self.postorder(root.right) 
      print(root.value)

  def search(self, root, value):
    if root == None:
      return print("value not present in BST")
    elif root.value == value:
      return print("-%s-",root.value)
    elif value <= root.value:
      self.search(root.left, value)
    elif value >= root.value:
      self.search(root.right, value)
    else:
      return "value not present in BST"
    



bst = BST()
bst.root = bst.insert(bst.root,5)
bst.insert(bst.root,3)
bst.insert(bst.root,2)
bst.insert(bst.root,4)
bst.insert(bst.root,7)
bst.insert(bst.root,6)
bst.insert(bst.root,8)


bst.inorder(bst.root)
print("---preorder--")
bst.preorder(bst.root)
print("---postorder--")
bst.postorder(bst.root)

print("---search--")
bst.search(bst.root,4)
bst.search(bst.root,9)

bst = BST()
bst.search(bst.root,5)

