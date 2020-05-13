class Node():
  def __init__(self,value):
    self.value = value
    self.next = None

#pop -> remove first node
#push -> add new in the top
#top -> return first item value
#isEmpty? -> check if the list is empty
class LinkedList():
  def __init__(self):
    self.head = None

  def push(self,value):
    current = self.head 
    if self.head == None:
      self.head = value
    else:
      while current.next:
        current = current.next
      current.next = value

  def pop(self):
    current = self.head 
    previous = None
    if self.head == None:
      print("list is empty")
    while current.next:
      previous = current
      current = current.next
    if self.head.next == None:
      self.head = None
    else:
      previous.next = None

  def top(self):
    current = self.head 
    if self.head != None:
      while current.next:
        current = current.next
      print("--top- %s",current.value)
    else:
      print("list is empty")

  def isEmpty(self):
    if self.head == None:
      return True
    else:
      return False


    

l= LinkedList()


l.push(Node(2))
l.push(Node(3))
l.push(Node(5))

l.pop()
l.top()

l.isEmpty()

l.pop()
l.top()
l.pop()
l.isEmpty()
l.top()