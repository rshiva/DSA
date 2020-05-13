class Node():
  def __init__(self,value):
    self.value = value
    self.next = None


class LinkedList():
  def __init__(self, head = None):
    self.head = head


  def append(self, node):
    current = self.head
    if self.head == None:
      self.head = node
    else:
      while current.next:
        current =  current.next
      current.next = node

  def prepend(self,node):
    if self.head == None:
      self.head = node
    else:
      current = self.head
      node.next = current
      self.head = node

  def add(self, position, node):
    counter = 0
    current = self.head
    while counter != position - 1:
      current = current.next
      counter+=1
    node.next = current.next
    current.next = node

  def search(self, value):
    current = self.head
    while current.value != value and current.next != None:
      print("---> current-value  %s" ,current.value )
      current = current.next
    if current.value == value:
      print("value --> ",current.value)
    else:
      print("%s not found in linked list -->",value)

    

  
  def delete(self, value):
    current = self.head
    while current.next.value != value:
      current = current.next
    if current.next.value == value:
      temp = current.next.next
      current.next = temp
    else:
      print("%s not found in linked list -->",value)




#Todo Search and delete



l= LinkedList()

l.append(Node(2))
l.append(Node(3))
l.append(Node(5))

l.prepend(Node(1))

l.add(3,Node(4))

l.search(3)

l.delete(3)

l.search(3)

node = l.head
while node:
  print(node.value)
  node = node.next


