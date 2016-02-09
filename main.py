from genome import genome
from utils import utils

# Instancier un genome
genome[] = neurone()

utils = utils()

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
