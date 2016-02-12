from __future__ import division
from random import randint
import random
from genome import *

# Initialiser aleatoirement les attributs de plusieurs individus
# contenus dans un tableau
def initialisation(individus):

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
def evaluation(individus):
	nbIndividus = len(individus)
	for i in range(0, nbIndividus):
		total=individus[i].getA() + individus[i].getB() + individus[i].getC()
		individus[i].setScore(total)
	return individus

# Selectionne deux parents a partir d'un tableau d'individus
# et renvoie un tableau avec les deux individus choisis
# Methode de selection : RWS (roulette)
def selectionneParentsRWS(parents):
	sumScore = 0
	nouveauxParents = []
	probabiliteCumule=0
	ListeProbabiliteCumule=[]

	for individu in parents:
		sumScore += individu.getScore()

	averageFitness = (float)(sumScore/len(parents))

	for indiv in parents:
		fitness = indiv.getScore()*100/sumScore
		probabiliteCumule+=fitness/sumScore
		ListeProbabiliteCumule.append(probabiliteCumule)

	while len(nouveauxParents) != 2:
		prob=random.random()

		for i in xrange(len(parents)):
			if ListeProbabiliteCumule[i-1]<prob<=ListeProbabiliteCumule[i]:
				nouveauxParents.append(parents[i])     

	return nouveauxParents

# Selectionne deux parents a partir d'un tableau d'individus
# et renvoie un tableau avec les deux individus choisis
# Methode de selection : tournoi
def selectionneParentsTournoi(parents):
	nbParents = len(parents)-1
	parentsTournoi = []
	parentsFinaux = [None, None]

	# On effectue 2 tournois pour avoir deux parents
	for roundTournoi in range(0,2):
		# Chaque tournoi est compose de 4 individus selectionnes au hasard
		for i in range(0, 4):
			parentsTournoi.append(parents[randint(0,nbParents)])

		# On effectue le tournoi : le meilleur gagne
		for i in range(0, 3):
			if parentsTournoi[i].getScore() > parentsTournoi[i+1].getScore():
				parentsFinaux[roundTournoi] = parentsTournoi[i]

			elif parentsTournoi[i].getScore() < parentsTournoi[i+1].getScore():
				parentsFinaux[roundTournoi] = parentsTournoi[i+1]

			else:
				parentsFinaux[roundTournoi] = parentsTournoi[i+randint(0,1)]
	
	return parentsFinaux


# Recois un tableau de deux individus et les croise
# pour retourner un enfant
def croisement(parents):
	#add random 50%
	enfant= Genome()
	newA = (parents[0].getA() + parents[1].getA())/2
	newB = (parents[0].getB() + parents[1].getB())/2
	newC = (parents[0].getC() + parents[1].getC())/2
	enfant.setA(newA)
	enfant.setB(newB)
	enfant.setC(newC)

	return enfant


# Modifie les attributs d'un tableau d'individus en fonction d'un
# taux de mutation passe en parametre (en pourcent)
def mutation(individus, taux=5):
	for i in range(0, len(individus)-1):
		individus[i].setA(variationValeur(individus[i].getA()))
		individus[i].setB(variationValeur(individus[i].getB()))
		individus[i].setC(variationValeur(individus[i].getC()))
	return individus

def variationValeur(valeur, taux=5):
	variation = randint(-taux, taux)/100
	valeur = valeur + valeur*variation
	return valeur

def printIndividus(individus):
	nbIndiv = len(individus)-1
	for i in range(0, nbIndiv):
		print("indiv%s: A=%s, B=%s, C=%s, score=%s" % 
			(i, individus[i].getA(), individus[i].getB(), individus[i].getC(), individus[i].getScore()))

def printIndividu(individu):
	print("indiv: A=%s, B=%s, C=%s, score=%s" % 
		(individu.getA(), individu.getB(), individu.getC(), individu.getScore()))
