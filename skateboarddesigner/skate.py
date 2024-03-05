from MainForm import *

class skate:
	def __init__(self):
		self._wheels1 = wheels1
		self._wheels2 = wheels2
		self._wheels3 = wheels3
		self._wheels4 = wheels4
		self._deck1 = deck1
		self._deck2 = deck2
		self._deck3 = deck3
		self._trucks1 = trucks1
		self._trucks2 = trucks2
		self._trucks3 = trucks3
		self._misc1 = misc1
		self._misc2 = misc2
		self._misc3 = misc3
		self._misc4 = misc4
		self._misc5 = misc5
		self._total = 0
	
	def wheelstot(self):
		if wheels1.isChecked():
			total += 20
		elif wheels2.isChecked():
			total += 22
		elif wheels3.isChecked():
			total += 24
		elif wheels4.isChecked():
			total += 28
		return total
		
	def deckstot(self):
		if deck1.isChecked():
			total += 45
		elif deck2.isChecked():
			total +=50
		elif deck3.isChecked():
			total += 60
		return total
		
	def truckstot(self):
		if trucks1.isChecked():
			total += 35
		elif trucks2.isChecked():
			total += 40
		elif trucks3.isChecked():
			total += 45
		return total
		
	def misctot(self):
		if misc1.isChecked():
			total += 10
		elif misc2.isChecked():
			total += 30
		elif misc3.isChecked():
			total += 2
		elif misc4.isChecked():
			total += 10
		elif misc5.isChecked():
			total += 3
		return total
	
	def total(self):
		self._total += self.wheelstot()
		self._total += self.deckstot()
		self._total += self.truckstot()
		self._total += self.misctot()
		return self._total
		

		
	
