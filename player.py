import entity
import reward
import item

class Player(entity.Entity):

	def __init__(self, health, location, inventory):
		entity.Entity.__init__(self, health)
		self.location = location
		self.inventory = inventory
		self.followers = []
		self.alive = True
		self.level = 1
		self.turn = 0
		self.pLocation = ""

		self.levelExperience = [100, 200, 400, 1000, 1500, 2000, 2500, 3000]

	def die(self):
		print(" \nGame Over")
		self.alive = False

	def levelUp(self):
		if self.inventory.experience == self.levelExperience[self.level-1]:
			self.inventory.experience -= self.levelExperience[self.level-1]
			self.level += 1
			print(f"You have leveled up! You are now level {self.level}")
			print(f"Reputation with the Pirate's Alliance has increased by 100")
			self.inventory.reputation += 100

	def reputationUp(self, reward):
		if self.inventory.reputation >= 2000 and self.inventory.reputationName == 'Neutral':
			self.inventory.reputation -= 2000
			print("You have become friendly with the Pirate's Alliance. As a token of their generosity, they gave 50 gold and 100 experience, as well as a cool looking hat.")
			reward = reward.Reward("Pirate's Alliance", 100, 50, 0, [item.Item("old pirate hat", "old but still gold", 22, 35)])

	def update(self):
		self.location.update()
		self.levelUp()
		self.reputationUp()