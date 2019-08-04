# Most basic class for all creatures; Larger class Stats will use class Stat for adding or subtracting different attributes from each entity.

class Stat:

	def __init__(self, attribute, value):
		self.attribute = attribute
		self.value = value
		self.addition = 0
		self.multiplication = 1

	def __str__(self):
		return f"{self.attribute}: {((self.value + self.addition) * self.multiplication)} points"

	def add(self, addAmount):
		self.addition += addAmount

	def mult(self, multAmount):
		self.multiplication += multAmount

	def returnValue(self):
		return ((self.value + self.addition) * self.multiplication)

	def notNone(self):
		if self.value == None:
			self.value = 0

# These are where the actual stats are defined, e.g. armor

class Stats:

	def __init__(self, health, explore, build, strength, intellect):
		self.health = Stat("health", health)
		self.explore = Stat("explore", explore)
		self.build = Stat("build", build)
		self.strength = Stat("strength", strength)
		self.intellect = Stat("intellect", intellect)

	def add(self, **kwargs):
		self.health.add(kwargs.get("health") if "health" else 0)
		self.explore.add(kwargs.get("explore") if "explore" else 0)
		self.build.add(kwargs.get("build") if "build" else 0)
		self.strength.add(kwargs.get("strength") if "strength" else 0)
		self.intellect.add(kwargs.get('intellect') if "intellect" else 0)

	def mult(self, **kwargs):
		self.health.mult(kwargs.get("health") if "health" else 0)
		self.explore.mult(kwargs.get("explore") if "explore" else 0)
		self.build.mult(kwargs.get("build") if "build" else 0)
		self.strength.mult(kwargs.get("strength") if "strength" else 0)
		self.intellect.mult(kwargs.get('intellect') if "intellect" else 0)