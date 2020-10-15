
# https://leetcode.com/problems/palindrome-number/

#1221
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
          return False
        reverted = 0
        while(x > reverted):
          reverted =  reverted * 10 + (x % 10)
          x = int(x/10)
          print("reverted,x",reverted,x)
        if x == reverted or x == int(reverted/10):
          return True
        else:
          return False


x=1221
s=Solution()
s.isPalindrome(x)

x=-1221
s=Solution()
s.isPalindrome(x)

x = 10
s=Solution()
s.isPalindrome(x)