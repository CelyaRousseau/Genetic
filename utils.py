from __future__ import division
from random import randint
from genome import *
import time
import random

# Initialiser aleatoirement les attributs de plusieurs individus
# contenus dans un tableau
def initialisation(individus):

	nbAttributs = individus[0].getNbAttributs()
	for i in range(0, len(individus)-1):
		attributs = []
		for j in range(0, nbAttributs):			
			attributs.append(randint(individus[i].getLowLimit(j), individus[i].getHighLimit(j)))
			time.sleep(0.05)
		individus[i].setAttributs(attributs)

	return individus

# Evalue chaque individus contenus dans un tableau et retourne un tableau
# de toutes les evaluations
def evaluation(individus):
	nbIndividus = len(individus)
	for i in range(0, nbIndividus):
		# on recupere tous les attributs
		attributs = individus[i].getAttributs()
		total=0
		# on calcule la somme des attributs : c'est le score de l'evaluation
		for j in range(0, len(attributs)):
			total += attributs[j]
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
	print("averageFitness : %s" %(averageFitness))

	for indiv in parents:
		fitness = indiv.getScore()*100/sumScore
		probabiliteCumule+=fitness/sumScore
		print("probabiliteCumule : %s" %(probabiliteCumule))
		ListeProbabiliteCumule.append(probabiliteCumule)

	while len(nouveauxParents) != len(parents):
		prob = random.random()

		for i in range(0, len(parents)-1):
			print("ListeProbabiliteCumule[i-1] : %s" %(ListeProbabiliteCumule[i-1]))
			if ListeProbabiliteCumule[i-1] < prob <= ListeProbabiliteCumule[i]:
				nouveauxParents.append(parents[i])
				print("parent : %s" %(parents[i]))   

	return nouveauxParents

# Selectionne deux parents a partir d'un tableau d'individus
# et renvoie un tableau avec les deux individus choisis
# Methode de selection : tournoi
def selectionneParentsTournoi(parents):
	nbParents = len(parents)
	parentsFinaux = [None, None]
	parentsSelected = [None, None]
	randoms = []

	# On effectue 2 tournois pour avoir deux lots de parents
	for roundTournoi in range(0,2):		
		# on prend 2 parents
		for i in range(0,2):
			# si on a un nombre impair d'individus, on clone le dernier
			if len(randoms) == len(parents)-1:
				parentsSelected[i] = parents[len(nbParents)-1]
			else:
				random = randint(0, nbParents-1)
				while random in randoms:
					random = randint(0, nbParents-1)
				randoms.append(random)
				parentsSelected[i] = parents[random]

		if parentsSelected[0].getScore() > parentsSelected[1].getScore():
			parentsFinaux[roundTournoi] = parentsSelected[0]
		else:
			parentsFinaux[roundTournoi] = parentsSelected[1]
	return parentsFinaux


# Recois un tableau de deux individus et les croise
# pour retourner un enfant
def croisement(parents, mode="moyenne"):
	#add random 50%
	enfant= Genome()
	newAttributs = []

	# ce mode croise les individus en faisant la moyenne de la somme de chaque attributs
	if mode == "moyenne":		
		parent1Attributs = parents[0].getAttributs()
		parent2Attributs = parents[1].getAttributs()
		for i in range(0, enfant.getNbAttributs()):
			valeur = (int)((parent1Attributs[i] + parent2Attributs[i])/2)
			newAttributs.append(valeur)
	# ce mode recupere aleatoirement l'attribut du parent 1 ou du parent 2
	else:
		nbAttributs = enfant.getNbAttributs()
		random = randint(0, nbAttributs)
		for i in range(0, nbAttributs):
			if i <= random:
				valeur = parents[0].getAttributs()[i]
			else:
				valeur = parents[1].getAttributs()[i]
			newAttributs.append(valeur)

	enfant.setAttributs(newAttributs)
	return enfant


# Modifie les attributs d'un tableau d'individus en fonction d'un
# taux de mutation passe en parametre (en pourcent)
def mutation(individus, taux=5):
	nbAttributs = individus[0].getNbAttributs()
	# pour chaque attribut on tire un nombre aleatoire compare au taux de mutation
	# en cas de mutation, on tire au hasard une nouvelle valeur dans les limites de l'attribut en question
	for i in range(0, len(individus)):
		for j in range(0, nbAttributs):
			random = randint(0,100)
			if random <= taux:
				attribs = individus[i].getAttributs()
				attribs[j] = randint(individus[i].getLowLimit(j), individus[i].getHighLimit(j))
				individus[i].setAttributs(attribs)
	return individus

# afficher un tableau d'individus
def printIndividus(individus):
	nbIndiv = len(individus)
	for i in range(0, nbIndiv):
		print("indiv%s: Attributs=%s, score=%s" % 
			(i, individus[i].getAttributs(), individus[i].getScore()))

# afficher un individu
def printIndividu(individu):
	print("indiv: Attributs=%s, score=%s" % 
			(i, individus[i].getAttributs(), individus[i].getScore()))

# afficher le resultat d'un croisement
def printCroisement(parent1, parent2, enfant):
	print("parent1          parent2         enfant")
	attributs1 = parent1.getAttributs()
	attributs2 = parent2.getAttributs()
	attributs3 = enfant.getAttributs()
	for i in range(0, parent1.getNbAttributs()):
		print("att%s=%s            att%s=%s          att%s=%s" %(i, attributs1[i], i, attributs2[i], i, attributs3[i]))
	print("----------------------------------------")

global lastRand
# tire un nombre aleatoire mais jamais 2 fois le meme a la suite
def randint(min, max):
	if not 'lastRand' in globals():
		lastRand = max+1

	r = random.randint(min, max)
   	while r == lastRand:
   	   r = random.randint(min, max)
   	lastRand= r
   	return r

def meilleurScore(individus):
	score = 0
	for indiv in individus:
		individuScore = indiv.getScore()
		if(individuScore > score):
			score = individuScore

	return score

def printIndicateurs(individus):
	individuScore = []
	for indiv in individus:
		individuScore.append(indiv.getScore())

	moy = sum(individuScore, 0.0) / len(individuScore)
	individuScoreCarre = [(indiv-moy)**2 for indiv in individuScore]
	vari = sum(individuScoreCarre, 0.0) / len(individuScoreCarre)
	ecart = vari**0.5

	print("moyenne : %s" %(moy))
	print("variance : %s" %(vari))
	print("ecart-type : %s" %(ecart))
	print("meilleur score : %s" %(meilleurScore(individus)))

		






