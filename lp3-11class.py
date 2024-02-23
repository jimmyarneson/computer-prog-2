class forklift:
  def __init__(self, desinging, coding, debuging, testing):
    self.desinging = desinging
    self.coding = coding
    self.debuging = debuging
    self.testing = testing
    self._time = 0
    self._percents = [0]*4

  def __percent(self, number):
    return round((number/self._time)*100 , 2)

  def calculate(self):
    self._time = self.desinging + self.coding + self.debuging + self.testing
    self._percents[0] = self.__percent(self.desinging)
    self._percents[1] = self.__percent(self.coding)
    self._percents[2] = self.__percent(self.debuging)
    self._percents[3] = self.__percent(self.testing)

  def display(self):
    print("Category\t\t\tTime")
    print(f"Desinging\t\t    {self._percents[0]}%")
    print(f"Coding\t\t\t    {self._percents[1]}%")
    print(f"Debuging\t\t    {self._percents[2]}%")
    print(f"Testing\t\t\t    {self._percents[3]}%")
    print(f"Total Time Spent: {self._time:.2f} miniutes")

def main():
  print("Enter the Amount of Time Spent on the Following: ")
  desining = float(input("Desining: "))
  coding = float(input("Coding: "))
  debuging = float(input("Debuging: "))
  testing = float(input("Testing: "))
  print()

  forkliftdriver = forklift(desining, coding, debuging, testing)
  forkliftdriver.calculate()
  forkliftdriver.display()

  pass


if __name__ == "__main__":
  main()