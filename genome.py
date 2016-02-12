
class Genome:

	def __init__(self):
		self.A = 1
	 	self.B = 1
	 	self.C = 1
	 	self.score = 0
	 	self.nbAttributs = 3

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

	# recuperer la limite basse d'un attribut
	def getLowLimit(self, param="1"):
		if param == "1":
			return self.lowLimitA
		elif param == "2":
			return self.lowLimitB
		else:
			return self.lowLimitC

	# recuperer la limite haute d'un attribut
	def getHighLimit(self, param="1"):
		if param == "1":
			return self.highLimitA
		elif param == "2":
			return self.highLimitB
		else:
			return self.highLimitC

	#recuperer tous les attributs
	def getAttributs(self):
		attribs = []
		attribs.append(self.A)
		attribs.append(self.B)
		attribs.append(self.C)
		return attribs

	# enregistrer tous les attributs
	def setAttributs(self, attributs):
		self.A = attributs[0]
		self.B = attributs[1]
		self.C = attributs[2]

	# recuperer le nombre d'attributs
	def getNbAttributs(self):
		return self.nbAttributs
