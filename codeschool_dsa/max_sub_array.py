#competetive_book
#Given an array of n numbers, our task is to calculate the maximum 
# subarray sum, i.e.,the largest possible sum of a sequence of consecutive values in the2
# array . The problem is interesting when there may be negative values in the
# array.  -1,2,4,-3,5,2-5,2


class Solution():
  def sum_subarray(self, parameter_list):
    best = 0
    addition = 0

    for i in range(0, len(parameter_list)):
      addition = max(parameter_list[i], addition+parameter_list[i])
      # print("parameter_list[i],addition--->",parameter_list[i],addition)
      best = max(addition, best)
      # print("Best", best)
    return best

s= Solution()
s.sum_subarray([-1,2,4,-3,5,2,-5,2])