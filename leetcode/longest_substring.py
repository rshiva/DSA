#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      #abcabcbb
      str_length = len(str)
      final_set = set()
      for i in range(0,str_length):
        print("i",i)
        inner_set = set()
        for j in range(i,str_length):
          print("j inner_set set",inner_set)
          if str[j] in inner_set:
            break
          else:
            inner_set.add(str[j]) 
        if len(inner_set) > len(final_set):
          final_set = inner_set
      print("final", final_set)
      return len(final_set)

str="pwwkew"          
Solution().lengthOfLongestSubstring(str1)
