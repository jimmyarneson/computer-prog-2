class Shape:
  #constructor: sets up class data
  def __init__(self, length, width):
    self.length = length
    self.width = width
    self._area = 0 # _ prefix basicaly means 'private'
    self._perim = 0 # it should only be called in the class

  # mutator/setter: modifies class data
  def calculate(self):
    self._area = self.length * self.width
    self._perim = 2 * self.length + 2 * self.width

  def setLength(self, length): #redudant
    self.length = length
    
  # Accessor/getter: returns class data
  def getArea(self):
    return self._area

  def getPerimeter(self):
    return self._perim


def main():
  len = int(input("Enter length: "))
  wid = int(input("Enter width: "))
  #make a new 'shape' object
  shape = Shape(len, wid) #call 'shape' constructor
  # shape.setLength(5)
  shape.calculate()
  print("Area: ", shape.getArea())
  print("Perimiter: ", shape.getPerimeter())
  pass

if __name__ == "__main__":
  main()