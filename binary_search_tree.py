# node -> value, left, right
# BST --> root/head
# insert -> root, data
# min and max
# delete a node
# search -> data
# inorder ->  left, root, right
# preorder -> root, left ,right
# postorder -> lef, right, root


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

  #level order
  # check two queue method
    def breadth_first(self,root):
      q = []
      q.append(root)
      if root == None:
        return "Empty"
      else:
        while len(q) != 0:
          current = q[0]
          print("-----%s",current.value)
          if current.left != None: 
            q.append(current.left)
          if current.right != None:
            q.append(current.right)
          q.pop(0)


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

    def min_max(self, search_type, root):
      if root == None:
        return "Empty"
      if search_type == "min":
        current = root
        while current.left != None:
          current = current.left
        print("min value %s", current.value)
      elif search_type == "max":
        current = root
        while current.right != None:
          current = current.right
        print("max value %s", current.value)
      
      
    def delete(self, node, value):
      # no child
      # one child
      # root is null
      root = node
      if root == None:
        return root
      if value > root.value:
        root.right = self.delete(root.right, value)
      elif value < root.value:
        root.left = self.delete(root.left, value)
      else:
        #no child
        if root.left == None and root.right == None:
          root = None
          return root
        #one child
        elif root.right == None:
          temp =  root
          root = root.left
          temp =  None
          return root
        elif root.left == None:
          temp =  root
          root = root.right
          temp =  None
          return root
        # two child
        else:
          temp = self.find_min(root.right)
          print("-temp- %s %s ",temp.value)
          root.value = temp.value
          root.right = self.delete(root.right, temp.value)
          return root


    def find_min(self, root):
      if root == None:
        return root
      else:
        current = root
        while current.right != None:
          current = current.right
        return current




bst = BST()
bst.root = bst.insert(bst.root,5)
bst.insert(bst.root,3)
bst.insert(bst.root,2)
bst.insert(bst.root,4)
bst.insert(bst.root,7)
bst.insert(bst.root,6)
bst.insert(bst.root,8)


bst.delete(bst.root, 7)


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

print("--level order--")
bst.breadth_first(bst.root)

print("min value") 
bst.min_max("min", bst.root)

print("max value") 
bst.min_max("max", bst.root)



