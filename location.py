import input
import globals

class Location:
	def __init__(self, zone, name, greeting):
		self.zone = zone
		self.name = name
		self.greeting = greeting

	def enter(self):
		print(self.greeting)

	def update(self):
		pass

def locationChange(options):
	# options = [["trek up the mountain", "summit", "yolo, I'm going up the mountain top"], ["sit down and poo", "toilet", "your destiny was to come to this very stall"]]
	inp = input.inputLines(options, lambda option: str(option[0])) - 1
	if (options[inp][2] != ""):
		print(options[inp][2])
	globals.player.location = options[inp][1]