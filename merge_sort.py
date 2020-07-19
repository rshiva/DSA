class MergeSort:
  
  def sort(self,list):
    list_size = len(list)
    if list_size < 2:
      return list
    mid = int(list_size/2)
    left = list[0:mid]  
    right = list[mid:list_size]
    sorted_left = self.sort(left)
    sorted_right = self.sort(right)
    sorted_list = self.merger(sorted_left, sorted_right, list)
    return sorted_list

  def merger(self,left, right, list):
    if(left and right):
      print("left", left)
      print("right",right)
      left_len = len(left)
      right_len = len(right)
      i,j,k = 0,0,0
      while( i < left_len and j < right_len):
        if left[i] <= right[j]:
          list[k] = left[i]
          i += 1
        else:
          list[k] = right[j]
          j += 1
        k += 1
      while(i < left_len):
        list[k] = left[i]
        i += 1
        k += 1 
      while(j < right_len):
        list[k] = right[j]
        j += 1
        k += 1
      return list


  

list=[2,4,2,1,6,8,5,3,7]
m = MergeSort()
m.sort(list)