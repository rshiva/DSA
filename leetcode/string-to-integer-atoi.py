#https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        result = ''
        s = s.strip()
        if len(s) == 0:
          return 0
        if s[0] == '-' or s[0] == '+' or ord(s[0]) in range(48,58):
          for i in range(0,len(s)):
            if i == 0 and (s[i] == '-' or s[i] == '+'):
              result = result + s[i]
            elif ord(s[i]) in range(48,58):
              result = result + s[i]
            elif ord(s[i]) == 46:
               result = result + s[i]
               return result.replace(".","")
            else:
              if result.isdigit():
                return int(result)
              else:
               return 0
            
        if (len(result) == 1 ) and (result == '+' or result == '-'):
          return 0
        result = result or 0
        return max(-2**31, min(int(result), 2**31-1))
      






str1 = "words and 987"
s=Solution()
s.myAtoi(str1)

str1 = "4231 for in words"
s=Solution()
s.myAtoi(str1)

str1 = "-91283472332"
s=Solution()
s.myAtoi(str1)

str1 = "3.4"
s=Solution()
s.myAtoi(str1)