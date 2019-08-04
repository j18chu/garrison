import random
import copy
import input

class Inventory:

	def __init__(self, gold = 0, experience = 0,reputation = 0, items = []):

		self.gold = gold
		self.reputation = reputation
		self.reputationName = 'Neutral'
		self.experience = experience
		self.items = items
		self.logs = 0
		self.stone = 0
		self.grass = 0
		self.quests = []

	def __str__(self):
		arr = [f"{self.gold} gold", f"{self.experience} experience", f"{self.reputation} reputation"]
		for i in self.items:
			arr.append(str(i))
		return '\n'.join(arr)

	def addGold(self, amount):
		self.gold += amount

	def addLogs(self, amount):
		self.logs += amount

	def addGrass(self, amount):
		self.grass += amount

	def addStone(self, amount):
		self.stone += amount

	def scavengeLogs(self, minimum, maximum, maxHarvest, numDuds, optionScavenge, optionNothing):
		back = False
		endNum = 0
		inpScavenge = 0
		while endNum <= maxHarvest and back == False:
			arr = []
			scavenge = False
			arr1 = copy.copy(optionScavenge)
			arr2 = copy.copy(optionNothing)
			while len(arr) != numDuds:
				
				
				if random.randint(1, 3) == 3 and scavenge == False:
					rand1 = arr1[random.randint(0, len(arr1)-1)]
					arr.append(rand1)
					arr1.remove(rand1)
					inpScavenge = len(arr)
					scavenge = True
				elif len(arr) == numDuds - 1 and scavenge == False:
					rand1 = arr1[random.randint(0, len(arr1)-1)]
					arr.append(rand1)
					arr1.remove(rand1)

					inpScavenge = len(arr)

				else:
					rand2 = arr2[random.randint(0, len(arr2)-1)]
					arr.append(rand2)
					arr2.remove(rand2)

			arr.append('Back')
			inp = input.inputLines(arr)

			if inp == inpScavenge:
				i = minimum
				while i < maximum:
					if (random.randint(1,3) == 1):
						i += 1
					else:
						endNum += i
						break
				if endNum >= maxHarvest:
					print(f"In total, you scavenged {endNum} logs")	
				else:
					print(f'You scavenged {i} logs.')
			elif inp == len(arr):
				if endNum == 1:
					print(f'In total, you scavenged {endNum} log.')
					back = True
				elif endNum == 0:
					print("You did not scavenge anything")
					back = True
				else:
					print(f'In total, you scavenged {endNum} logs.')
					back = True
				
				break
			else:
				print("Due to your relaxation, you did not collect any logs.")
		self.logs += endNum


#scavengeLogs(2, 4, 15, 5, ["Chop down a tree", "Collect driftwood", "Scavenge for sticks"], ["Relax", "Sit down", "Do nothing", "Fall asleep", "Daydream", "Think about how many rest phrases I can come up with", "Contemplate life", "Stop", "Watch a large, red beetle"])


	def scavengeStone(self, minimum, maximum, maxHarvest, numDuds, optionScavenge, optionNothing):
		back = False
		endNum = 0
		inpScavenge = 0
		while endNum <= maxHarvest and back == False:
			arr = []
			scavenge = False
			arr1 = copy.copy(optionScavenge)
			arr2 = copy.copy(optionNothing)
			while len(arr) != numDuds:
				
				
				if random.randint(1, 3) == 3 and scavenge == False:
					rand1 = arr1[random.randint(0, len(arr1)-1)]
					arr.append(rand1)
					arr1.remove(rand1)
					inpScavenge = len(arr)
					scavenge = True
				elif len(arr) == numDuds - 1 and scavenge == False:
					rand1 = arr1[random.randint(0, len(arr1)-1)]
					arr.append(rand1)
					arr1.remove(rand1)

					inpScavenge = len(arr)

				else:
					rand2 = arr2[random.randint(0, len(arr2)-1)]
					arr.append(rand2)
					arr2.remove(rand2)

			arr.append('Back')
			inp = input.inputLines(arr)

			if inp == inpScavenge:
				i = minimum
				while i < maximum:
					if (random.randint(1,3) == 1):
						i += 1
					else:
						endNum += i
						break
				if endNum >= maxHarvest:
					print(f"In total, you scavenged {endNum} stone")	
				else:
					print(f'You scavenged {i} stone.')
			elif inp == len(arr):
				if endNum == 1:
					print(f'In total, you scavenged {endNum} stone.')
					back = True
				elif endNum == 0:
					print("You did not scavenge anything")
					back = True
				else:
					print(f'In total, you scavenged {endNum} stone.')
					back = True
				
				break
			else:
				print("Due to your relaxation, you did not collect any stone.")
		self.stone += endNum

	def scavengeGrass(self, minimum, maximum, maxHarvest, numDuds, optionScavenge, optionNothing):
		back = False
		endNum = 0
		inpScavenge = 0
		while endNum <= maxHarvest and back == False:
			arr = []
			scavenge = False
			arr1 = copy.copy(optionScavenge)
			arr2 = copy.copy(optionNothing)
			while len(arr) != numDuds:
				
				
				if random.randint(1, 3) == 3 and scavenge == False:
					rand1 = arr1[random.randint(0, len(arr1)-1)]
					arr.append(rand1)
					arr1.remove(rand1)
					inpScavenge = len(arr)
					scavenge = True
				elif len(arr) == numDuds - 1 and scavenge == False:
					rand1 = arr1[random.randint(0, len(arr1)-1)]
					arr.append(rand1)
					arr1.remove(rand1)

					inpScavenge = len(arr)

				else:
					rand2 = arr2[random.randint(0, len(arr2)-1)]
					arr.append(rand2)
					arr2.remove(rand2)

			arr.append('Back')
			inp = input.inputLines(arr)

			if inp == inpScavenge:
				i = minimum
				while i < maximum:
					if (random.randint(1,3) == 1):
						i += 1
					else:
						endNum += i
						break
				if endNum >= maxHarvest:
					print(f"In total, you scavenged {endNum} grass")	
				else:
					print(f'You scavenged {i} grass.')
			elif inp == len(arr):
				if endNum == 1:
					print(f'In total, you scavenged {endNum} log.')
					back = True
				elif endNum == 0:
					print("You did not scavenge anything")
					back = True
				else:
					print(f'In total, you scavenged {endNum} grass.')
					back = True
				
				break
			else:
				print("Due to your relaxation, you did not collect any grass.")
		self.grass += endNum


	def addExperience(self, amount):
		self.experience += amount

	def addReputation(self, amount):
		self.reputation += amount

	def removeGold(self, amount):
		if self.gold < amount:
			return False
		else:
			self.gold -= amount
			return True

	def removeLogs(self, amount):
		if self.logs < amount:
			return False
		else:
			self.logs -= amount
			return True


	def removeStone(self, amount):
		if self.stone < amount:
			return False
		else:
			self.stone -= amount
			return True

	def removeGrass(self, amount):
		if self.grass < amount:
			return False
		else:
			self.grass -= amount
			return True


	def addItem(self, item):
		for i in self.items:
			if i.stack(item):
				return 
		self.items.append(item)

	def removeItem(self, item, amount = 1):
		for i in self.items:
			if i.remove(item, amount):
				if i.number == 0:
					self.items.remove(i)
				return True
		return False

	def usable(self):
		usable = []
		for i in self.items:
			if i.usable:
				usableItems.append(i)
		return usable

	def removeByName(self, name, number):
			for item in self.items:
				if item.name == name and item.number >= number:
					item.number -= number
					if item.number == 0:
						self.items.remove(item)
					return True
				return False