class Bubble():

#Time complexity best case O(n), average and worst case O(n^2)

  def sort(self, list):
    for i in range(len(list)):
      flag = 0
      for j in range(len(list)-i-1):
        if list[j] > list[j+1]:
          print(list[j], list[j+1])
          list[j], list[j+1] = list[j+1], list[j]
          flag = 1
      if flag == 0:
        return list
        break
    



# list = [4, 3, 5, 7, 1]
# sorted_list = [1,2,3,4]
# b = Bubble()
# b.sort(sorted_list)

