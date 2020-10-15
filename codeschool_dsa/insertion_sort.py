class Insertion:
  # worst case - time complexity O(n^2)
  # keep the sorted list in the left and unsorted in right
  def sort(self, list):
    list_size = len(list)
    for i in range(1,list_size):
      value = list[i] 
      position = i
      while (position > 0 and list[position-1] > value):
       list[position] = list[position-1]
       position = position - 1 
      
      list[position] = value
    return list
      
    


