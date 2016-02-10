from genome import genome
from utils import utils

# Instancier un genome
individus = []

utils = utils()


individus.append(genome())
individus.append(genome())
individus.append(genome())
individus.append(genome())
individus.append(genome())
# tester l'initialisation
individus = utils.initialisation(individus)
print("initialisation=%s" % individus)

# tester l'evaluation
individus = utils.evaluation(individus)
print("evaluation=%s" % individus)

# tester selection rws

# tester selection tournoi
parents = []
parents = utils.selectionneParentsTournoi(individus)
print("parents=%s" % parents)

# tester croisement
enfant = utils.croisement(parents)
print("enfant=%s" % enfant)

#testion mutation
mute = []
mute.append(enfant)
muted = utils.mutation(mute)
print("muted=%s" % muted)

'''
# initialise les individus
individus = utils.initialisation()
# Evalue la population de base
individusSelection = Selectinutils.evaluation(individus)

while(){
	# Selectionne les parents
	parents = utils.selectionneParentsRWS(individusSelection)
	enfants = [100]

	for x in xrange(1,100):
		# Effectue un croisement
		enfants += utils.croisement()

	# Applique une mutation 
	individus = utils.mutation(enfants)
	# Evalue les individus
	individusSelection = utils.evaluation(individus)
}
'''
