from genome import *
from utils import *

#MODE = "tournoi"
MODE = "RWS"
#MODECROISEMENT = "moyenne"
MODECROISEMENT = "aleatoire"
NBINDIVIDUS = 5
DEBUG = 0
SCORE_VOULU = 30

# Instancier un genome
individus = []
for i in range(0,NBINDIVIDUS):
	individus.append(Genome())

# tester l'initialisation
individus = initialisation(individus)
print("\ninitialisation : ")
printIndividus(individus)

# tester l'evaluation
individus = evaluation(individus)
if DEBUG:
	print("\nevaluation : ")
	printIndividus(individus)

j=0
while j != -1:
	j+=1
	parents = []
	enfants = []

	if DEBUG:
		print("\ncroisement : ")
	for i in range(0,NBINDIVIDUS):
		if MODE == "tournoi":
			# tester selection tournoi
			parents = selectionneParentsTournoi(individus)
		else:
			# tester selection rws
			parents = selectionneParentsRWS(individus)
		# tester croisement
		enfant = croisement(parents, MODECROISEMENT)
		enfants.append(enfant)
		if DEBUG:
			printCroisement(parents[0], parents[1], enfant)

	#tester mutation
	muted = mutation(enfants)
	if DEBUG:
		print("\nmuted : ")
		printIndividus(muted)

	# tester l'evaluation
	individus = evaluation(muted)
	if DEBUG:
		print("\nevaluation : ")
		printIndividus(individus)

	print("\ngeneration %s" %(j-1))
	printIndicateurs(individus)

	score = meilleurScore(individus)
	if score >= SCORE_VOULU:
		printIndividus(individus)
		j=-1




