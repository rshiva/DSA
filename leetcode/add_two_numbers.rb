# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val = 0, _next = nil)
      @val = val
      @next = _next
  end
end
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
  carry = 0
  node = head = ListNode.new()
    while(l1.val or l2.val or carry) do
      sum = l1.val + l2.val + carry
      carry = sum/10
      sum = sum%10
      node.next = sum
      l1 = l1.next
      l2 = l2.next
    end
  return head.next
end