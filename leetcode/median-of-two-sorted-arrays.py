# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        print(nums1, nums2)
        final_array = nums1 + nums2
        final_array.sort()
        len_array = len(final_array)
        if len_array != 0:
          if len_array % 2 == 0:
            result = (final_array[int(len_array/2)-1] + final_array[int(len_array/2)])/2
            return result if result > 0 else 0
          else:
            return final_array[int(len_array/2)]
        else:
          return 0


# array1 = [0,0,0,0,0]
# array2 = [-1,0,0,0,0,0,1]
# s = Solution()
# s.findMedianSortedArrays(array1, array2)

# array1=[1,2]
# array2= [3,4]
# s = Solution()
# s.findMedianSortedArrays(array1, array2)
