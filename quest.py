import globals
import input

class Quest():
	def __init__(self, name, accept, progress, end, reward, conditionAccept = False, conditionEnd = False, autoGive = False):
		self.name = name
		self.accept = accept
		self.progress = progress
		self.end = end
		self.complete = 'accept'
		self.reward = reward
		self.visible = False
		self.conditionAccept = conditionAccept
		self.conditionEnd = conditionEnd
		self.autoGive = autoGive
		self.completed = False


	def setVisible(self):
		if self.conditionAccept(globals.player) == True:
			self.visible = True

	def checkAuto(self):
		if autoGive == True:
			self.complete = 'progress'
			return True
		return False

	def checkIn(self):
		self.checkAuto
		if self.visible == True :
			if (self.conditionEnd(globals.player)) == True and self.completed == False:
					self.rewarded()
					globals.player.inventory.quests.remove(self.name)
					self.completed = True
					self.complete = 'end'
			if (self.complete == 'accept'):
				inp = input.inputLines(["Accept", "Decline"])
				if inp == 1:
					print('<Quest Accepted>')
					self.complete = 'progress'
				else:
					return
			elif (self.complete == 'progress'):
				print(self.progress)

	def rewarded(self):
		print(self.end)
		print(f"You completed the quest '{self.name}'.")
		self.reward.giveReward()
