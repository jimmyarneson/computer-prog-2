
class pizza:
	def __init__(self, num1):
		self._num1 = num1
		self._pizza = 0
		self._labor = 0.75
		self._rent = 1.00
		self._materials = 0.05 * num1 ** 2.0
		
		
	def calculate(self):
		return self._materials
	
	def getTotal(self):
		return self._labor + self._rent + self._materials
