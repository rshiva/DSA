class Solution:
  def bSearch(self, array, num) -> bool:
    if len(array) == 0:
      return False
    mid = round(len(array)/2)
    if array[mid] == num:
      return True
    elif array[mid] < num:
      self.bSearch(array[mid:], num)
    elif array[mid] > num:
      self.bSearch(array[:mid], num)
    else:
      return False 


s= Solution()
a = [1,3,6,9,11,20]
s.bSearch(a, 20)