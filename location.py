import input
import globals

class Location:

	def __init__(self, zone, name, openText):
		self.zone = zone
		self.name = name
		self.openText = openText
		self.returnText = ""

	def onReturn(self, options):
		# options = ["Actual text", past Location]
		pass


	def text(self):
		if self.returnText != "":
			input.printInput(self.returnText)
		else:
			input.printInput(self.openText)
		self.returnText = ""


	def update(self):
		pass

	

def locationChange(options):
	# options = [["trek up the mountain", "summit", "yolo, I'm going up the mountain top"], ["sit down and poo", "toilet", "your destiny was to come to this very stall"]]
	inp = input.inputLines(options, lambda option: str(option[0])) - 1
	if (options[inp][2] != ""):
		input.printInput(options[inp][2])

	globals.player.pLocation = globals.player.location
	globals.player.location = options[inp][1]


class HarvestLocation:

	def __init__(self, zone, name, openText):
		self.zone = zone
		self.name = name
		self.openText = openText
		self.returnText = ""
		self.maxHarvest = 0

	def onReturn(self, text):
		pass

	def text(self):
		if self.returnText != "":
			input.printInput(self.returnText)
		else:
			input.printInput(self.openText)
		self.returnText = ""


	def update(self):
		pass
