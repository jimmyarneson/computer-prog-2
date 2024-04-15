class Salesperson:
  def __calc(self):
    if self.code == 5 or self.code == 8:
      if self.sales <= 5000:
        self._commision = self.sales * 0.075
      else:
          self._commision = 5000 * 0.075 + (self.sales-5000) * 0.085
    elif self.code == 17:
      if self.sales <= 3500:
        self._commision = self.sales * 0.095
      else:
        self._commision = 3500 * 0.095 + (self.sales-3500) *0.12


  def __init__(self, id, code, sales):
    self.id = id
    self.code = code
    self.sales = sales
    self._commision = 0

  def setComm(self):
    self.__calc()

  #override the str() dunder/magic method(tostring)
  def __str__(self):
    return f"{self.id}\t\t{self.code}\t\t{self.sales}\t{self._commision}"