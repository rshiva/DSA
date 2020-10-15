class Solution:
    def convert(self, s: str, numRows: int) -> str:
      final_array = [""] * numRows

      if numRows == 1 or numRows >= len(s):
        return s
      index, step = 0, 1
      for x in s:
        final_array[index] += x
        if index == 0:
          step = 1
        elif index == numRows - 1:
          step = -1
        index = index + step
      return ''.join(final_array)
        
      


input= "PAYPALISHIRING"
s=Solution()
s.convert(input,3)

      

