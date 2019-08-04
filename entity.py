# In this game, you are a pirate of an unknown class. This is a create your own world game where you decide which buildings to build, who to recruit, what to farm and mine,
# All while your reputation grows. Followers of different class and name modifier will join your crew, with different specialties.

import stats
# The entity class will set the general parameters for every creature. Later, child classes will be made of the parent class Entity. Entity uses Stats to modify health

class Entity():
	def __init__(self, health, **kwargs):
		self.name = '' 
		self.health = health
		self.modifier = ''
		self.specialty = ''
		self.stats = stats.Stats(
			health,
			kwargs.get("explore") if "explore" else 0,
			kwargs.get("build") if "build" else 0,
			kwargs.get("strength") if "strength" else 0,
			kwargs.get("intellect") if "intellect" else 0
			)
	

	def notNone(self):
		self.stats.explore.notNone()
		self.stats.build.notNone()
		self.stats.strength.notNone()
		self.stats.strength.notNone()
