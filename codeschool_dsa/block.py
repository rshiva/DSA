class Block():
  def draw(self, num: int):

    if num == 0:
      return
    self.draw(num-1)
    print(num*"#")
  

b=Block()
b.draw(4)

class Block():
  def draw(self, num: int):

    for i in range(1,num):{
      print(i*"#")
    }


b=Block()
b.draw(4)





