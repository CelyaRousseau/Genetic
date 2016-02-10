
class Genome:
	A = 1
	B = 1
	C = 1
	score = 0

	lowLimitA = 0
	highLimitA = 10
	lowLimitB = 0
	highLimitB = 10
	lowLimitC = 0
	highLimitC = 10

	def __new__(self):
		self.A = 1
	 	self.B = 1
	 	self.C = 1
	 	self.score = 0

	 	self.lowLimitA = 0
	 	self.highLimitA = 10
	 	self.lowLimitB = 0
	 	self.highLimitB = 10
	 	self.lowLimitC = 0
	 	self.highLimitC = 10


 	def display(self):
 		# TODO : implement display
 		return 0	

	def setScore(self, score):
		self.score = score

	def getScore(self):
		return self.score

	def getA(self):
		return self.A

	def getB(self):
		return self.B

	def getC(self):
		return self.C

	def setA(self, A):
		self.A = A

	def setB(self, B):
		self.B = B

	def setC(self, C):
		self.C = C

	def getLowLimit(self, param="A"):
		if param == "A":
			return self.lowLimitA
		elif param == "B":
			return self.lowLimitB
		else:
			return self.lowLimitC

	def getHighLimit(self, param="A"):
		if param == "A":
			return self.highLimitA
		elif param == "B":
			return self.highLimitB
		else:
			return self.highLimitC