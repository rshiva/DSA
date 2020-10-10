#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# l1 = [2,4,3], l2 = [5,6,4]
class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      carry = 0
      node = head = ListNode(0)
      while l1 or l2 or carry:
        val1 = l1.val  if l1 else 0
        val2 = l2.val  if l2 else 0
        add = val1 + val2 + carry
        carry = add//10
        add = add % 10
        node.next = ListNode(add)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None 
        node = node.next
        if carry == 1:
            node.next = carry
      return head.next
      


