class animal:
  def __init__(self, name, favW):
    self._name = name
    self._favW = favW

  def getName(self):
    return self._name

class hiccas(animal):
  def __init__(self, name, favW, furM):
    super.__init__(name, favW)
    self.furM = furM

class wallies(animal):
  def __init__(self, name, favW, steps):
    super.__init__(name, favW)
    self.steps = steps

class beepers(animal):
  def __init__(self, name, favW, sWord):
    super.__init(name, favW)
    self.sWord = sWord