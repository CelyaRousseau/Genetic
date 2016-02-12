from genome import *
from utils import *

MODE = "tournoi"
#MODE = "RWS"
NBINDIVIDUS = 5

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
print("\nevaluation : ")
printIndividus(individus)

# tester selection rws


parents = []
enfants = []
print("\ncroisement : ")
for i in range(0,NBINDIVIDUS):
	if MODE == "tournoi":
		# tester selection tournoi
		parents = selectionneParentsTournoi(individus)
	else:
		# tester selection rws
		parents = selectionneParentsRWS(individus)
	# tester croisement
	enfant = croisement(parents)
	enfants.append(enfant)
	printCroisement(parents[0], parents[1], enfant)

#tester mutation
muted = mutation(enfants)
print("\nmuted : ")
printIndividus(muted)

# tester l'evaluation
muted = evaluation(muted)
print("\nevaluation : ")
printIndividus(muted)

