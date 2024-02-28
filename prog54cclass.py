class fortnite:

  def __init__(self, radius):
    self.radius = radius
    self.area = 0
    self.cir = 0

  def calculate(self):
    self.area = self.radius * 3.14 ** 2
    self.cir = 3.14 * 2 ** self.radius

  def getCir(self):
    return self.cir

  def getArea(self):
    return self.area
    
def main():
   rad = float(input("Enter the Radius: "))
   fortnit = fortnite(rad)
   fortnit.calculate()
   print("Area: ", round(fortnit.getArea(),2))
   print("Circumfrence: ", round(fortnit.getCir(),2))

   pass


if __name__ == "__main__":
  main()