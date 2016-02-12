from genome import *
from utils import *

# Instancier un genome
individus = []

individus.append(Genome())
individus.append(Genome())
individus.append(Genome())
individus.append(Genome())
individus.append(Genome())
# tester l'initialisation
individus = initialisation(individus)
print("\ninitialisation=")
printIndividus(individus)


# tester l'evaluation
individus = evaluation(individus)
print("\nevaluation=")
printIndividus(individus)

# tester selection rws

# tester selection tournoi
parents = []
enfants = []

for i in range(0,5):
	parents = selectionneParentsRWS(individus)
	# tester croisement
	enfants.append(croisement(parents))

print("\nenfant=")
printIndividus(enfants)

#tester mutation
muted = mutation(enfants)
print("\nmuted=")
printIndividus(muted)

# tester l'evaluation
muted = evaluation(muted)
print("\nevaluation=")
printIndividus(muted)

'''
# initialise les individus
individus = initialisation()
# Evalue la population de base
individusSelection = Selectinevaluation(individus)

while(){
	# Selectionne les parents
	parents = selectionneParentsRWS(individusSelection)
	enfants = [100]

	for x in xrange(1,100):
		# Effectue un croisement
		enfants += croisement()

	# Applique une mutation 
	individus = mutation(enfants)
	# Evalue les individus
	individusSelection = evaluation(individus)
}
'''

