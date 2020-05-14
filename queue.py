class Node():
  def __init__(self,value):
    self.value = value
    self.next = None


#enqueue #add
#dequeue #remove
#isEmpty
#peek

class QueueLinkedList():
  def __init__(self):
    self.head = None


  def enqueue(self,value):
    current = self.head
    if self.head == None:
      self.head = value
    else:
      while current.next:
        current = current.next
      current.next = value

  def dequeue(self):
    if not self.isEmpty():
      current = self.head
      if self.head != None and current.next:
        next_node = current.next
        self.head =  next_node
      else:
        self.head = None
    else:
      print("Queue is empty")

  def isEmpty(self):
    if self.head == None:
      return True

  def peek(self):
    if self.head:
      return self.head.value


l= QueueLinkedList()


l.enqueue(Node(2))
l.enqueue(Node(3))
l.enqueue(Node(5))

l.dequeue()
l.peek()

l.isEmpty()

l.dequeue()
l.peek()
l.dequeue()
l.isEmpty()
l.peek()


node = l.head
while node:
  print(node.value)
  node = node.next
    