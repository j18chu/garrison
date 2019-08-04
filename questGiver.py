import globals
import input
import quest

class QuestGiver():

	def __init__(self, name, openText, quests, pLocation):
		self.name = name
		self.openText = openText
		self.quests = quests
		# Past location
		self.pLocation = pLocation
		self.showOpenText = False
		self.isSame = False

	def locationBack(self, location):
		globals.player.location = self.pLocation

	def openName(self):
		
		arr = []
		isSame = True
		if self.showOpenText == False:
			print(self.openText)
			self.showOpenText = True
		print("")
		print("Quest:")
		for i in range(len(self.quests)):
			if self.quests[i].completed == False:
				for i in range(len(self.quests)):
					self.quests[i].setVisible()
				for i in range(len(self.quests)):
					if self.quests[i].visible == True and self.quests[i].complete == 'progress':
						arr.append(f'{self.quests[i].name} (in progress)')
						if self.isSame == False:
							globals.player.inventory.quests.append(self.quests[i].name)
							self.isSame = True

					elif self.quests[i].visible == True:
						arr.append(self.quests[i].name)

		arr.append('Back')
		

		inp = input.inputLines(arr)
		i = 1
		while i < len(arr):
			if (inp == i):
				self.quests[i-1].checkIn()
				self.openName()
			i+=1
		if inp == (i+1):
			locationBack(self.pLocation)

			

