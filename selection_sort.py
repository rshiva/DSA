class Selection:
# time complexity O(n^2)

  def sort(self,list):
    print("list", list)
    for i in range(len(list)):
      minindex = i
      for j in range(i+1, len(list)):
        if list[minindex] > list[j]:  
          minindex = j
      list[i], list[minindex] = list[minindex], list[i]
    return list


# s = Selection()
# s.sort([4,3,5,7,1])


#4,3,5,7