class Solution:
  def countingSort(self, array):
    """
    The algorithm creates a bookkeeping array, 
    whose indices are elements of the original array. 
    The algorithm iterates through the original array and 
    calculates how many times each element appears in the array.
    """
    mx = max(array)
    # mn = min(array)
    new_array = [0] * (mx+1)
    for i in range(0,len(array)):
      if new_array[array[i]] != 0:
        new_array[array[i]] = new_array[array[i]] + 1
      else:
        new_array[array[i]] = 1
    return new_array


s=Solution()
s.countingSort([1,3,6,9,9,3,5,9])