class responsibility:
  def __init__(self, kwh):
    self.kwh = kwh
    self._cost = 0

  def calc(self):
    if 0 <= self.kwh <= 2000:
      self._cost += 0.07 * self.kwh
    elif 2000 < self.kwh <= 9999:
      self._cost += 2000 * 0.07 + (self.kwh -2000) * 0.05 
    elif self.kwh > 10000:
      self._cost += 2000 * 0.07 + 8000 * 0.05 + (self.kwh -10000) * 0.04
    

  def __str__(self):
    return f"The cost of {self.kwh} is {round(self._cost , 2)}"