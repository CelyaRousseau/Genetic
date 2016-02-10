from random import randint

class utils:


	def __init__(self):

	# Initialiser aleatoirement les attributs de plusieurs individus
	# contenus dans un tableau
	def initialisation(self, individus):

		for i in range(0, len(individus)-1):
			rand = randint(individus[i].getLowLimit("A"), individus[i].getHighLimit("A"))
			individus[i].setA(rand)

			rand = randint(individus[i].getLowLimit("B"), individus[i].getHighLimit("B"))
			individus[i].setB(rand)

			rand = randint(individus[i].getLowLimit("C"), individus[i].getHighLimit("C"))
			individus[i].setB(rand)

		return individus

	# Evalue chaque individus contenus dans un tableau et retourne un tableau
	# de toutes les evaluations
	def evaluation(self, individus):
		eval=[]
		for i in range(0, len(individus):
			total=individus[i].getA() + individus[i].getB() + individus[i].getC()
			individus[i].setScore(total)

	# Selectionne deux parents a partir d'un tableau d'individus
	# et renvoie un tableau avec les deux individus choisis
	# Methode de selection : RWS (roulette)
	def selectionneParentsRWS(self, parents):
	# for all members of population
	#     sum += fitness of this individual
	# end for
	    
	# for all members of population
	#     probability = sum of probabilities + (fitness / sum)
	#     sum of probabilities += probability
	# end for
	    
	# loop until new population is full
	#      do this twice
	#          number = Random between 0 and 1
	#        for all members of population
	#            if number > probability but less than next probability 
	#                 then you have been selected
	#        end for
	#      end
	#      create offspring
	# end loop
		for individu in xrange(0,len(parents):
			sum += individu.getScore()

		for x in xrange(0,len(parents)):
			pr

		parentsFinaux = [parents[0], parents[1]]
		return parentsFinaux

	# Selectionne deux parents a partir d'un tableau d'individus
	# et renvoie un tableau avec les deux individus choisis
	# Methode de selection : tournoi
	def selectionneParentsTournoi(self, parents):
		nbParents = len(parents)-1
		parentsTournoi = []
		parentsFinaux = [None, None]

		# On effectue 2 tournois pour avoir deux parents
		for roundTournoi in range(0,1):
			# Chaque tournoi est compose de 4 individus selectionnes au hasard
			for i in range(0, 4):
				parentsTournoi.append(parents[randint(0,nbParents)])

			# On effectue le tournoi : le meilleur gagne
			for i in range(0, 4):
				if parentsTournoi[i].getScore() > parentsTournoi[i+1].getScore():
					parentsFinaux[roundTournoi] = parentsTournoi[i]

				elif parentsTournoi[i].getScore() < parentsTournoi[i+1].getScore():
					parentsFinaux[roundTournoi] = parentsTournoi[i+1]

				else:
					parentsFinaux[roundTournoi] = parentsTournoi[i+randint(0,1)]
		
		return parentsFinaux


	# Recois un tableau de deux individus et les croise
	# pour retourner un enfant
	def croisement(self, parents):
		enfant= genome()
		newA = (parents[0].getA() + parents[1].getA())/2
		newB = (parents[0].getB() + parents[1].getB())/2
		newC = (parents[0].getC() + parents[1].getC())/2
		enfant.setA(newA)
		enfant.setB(newB)
		enfant.setC(newC)

		return enfant


	# Modifie les attributs d'un tableau d'individus en fonction d'un
	# taux de mutation passe en parametre (en pourcent)
	def mutation(self, individus, taux=5):
		for i in range(0, len(individus)-1):
			individus[i].setA(variationValeur(individus[i].getA()))
			individus[i].setB(variationValeur(individus[i].getB()))
			individus[i].setC(variationValeur(individus[i].getC()))
		return individus

	def variationValeur(self, valeur, taux=5):
		variation = randint(-taux, taux)/100
		valeur = valeur + valeur*variation
		return valeur

