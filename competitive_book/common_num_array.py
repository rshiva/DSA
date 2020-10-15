class Solution():

  def solution1(self, array1, array2):
    result=0
    s1 = set(array1)
    s2 = set(array2)
    print(s1,s2)
    for i in range(0, len(array1)):
      if (array1[i] in s1) and (array1[i] in s2):
        # result.append(array1[i])
        result = result+1
    return result


s=Solution()
s.solution1([0,6,3,10],[1,2,7,9,10,3,0])