class person:
  def __init__(self,fn,ln):
    self._first = fn
    self._last = ln

  def getName(self):
    return self._first + " " + self._last

class student(person):
  def __init__(self, fn, ln, gpa):
    super().__init__(fn, ln)
    self.gpa = gpa

class teacher(person):
  def __init__(self, fn, ln, numS):
    super().__init__(fn, ln)
    self.numStudent = numS

class administrator(person):
  def __init__(self, fn, ln, favW):
    super().__init__(fn, ln)
    self.favWord = favW