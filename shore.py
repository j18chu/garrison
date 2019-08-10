import globals
import questGiver
import input
import quest
import item
import random
import reward
import location

oldMan = questGiver.QuestGiver("Old Man", "Doesn't matter where I came from. Doesn't matter where you came from, for that matter. All that matters is you're here to help me.",
	[quest.Quest('Destroy the Brush',
	'An evil enemy known as the brush has taken over that hill over there. Go clear it for me, will you? I will know you did the deed if you bring me 12 grass clumps. There might even \nbe something in it for you.',
	'Have you destroyed the brush over on that hill over there and brought me my 12 grass clumps?',
	"Not bad, not bad. Here's the reward I promised you. You can also keep half the grass you collected.",
	reward.Reward("oldMan", globals.player, 50, 100, 50, [item.Item("old gold coin", "it's a coin", 5, 15)], logs = 10, grass = 6),
	lambda player : player.level >= 1,
	lambda player : player.inventory.removeGrass(12))],
	globals.player.pLocation)

class ForgottenShore(location.Location):
	def __init__(self):
		location.Location.__init__(self, "Abandoned Shoals", "The Forgotten Shore", "The first thing you feel when you awake is a splitting headache. You slowly open your eyes, taking in the sand below you, the palm trees ringing your vision, and the small\ncrabs scuttling around you. You shut your eyes and massage your temples, trying to recall what happened. The last thing you remember was sailing the Blue Seas with your crew, being\nuniversally feared, and then the crash. You open your eyes up again, this time noticing the wreckage around you.\n")

	def update(self):
		self.text()
		self.appendToArray()
		location.locationChange([['Explore the wreckage', WreckedShore, '', False], ['Close your eyes for a little longer', Death, 'While you rest, a group of savages appear on the beach. Grotesquely dressed, they creep up on you. The one with the mask, clearly the leader, motions them towards you. No one hears your scream as they pummel you.', False]])

ForgottenShore = ForgottenShore()

class WreckedShore(location.Location):
	def __init__(self):
		location.Location.__init__(self, "Abandoned Shoals", "The Wrecked Shore", 'You walk around until you notice a plank of wood, larger than the rest. You turn it over and it reveals a name: The S.S. Furybringer. You finally remember who you were. You were a notorious captain who was as fearsome as he was cunning. You were able to recruit followers and pillage entire islands. You sigh, thinking about how all this is behind you. You notice a path ahead of you.')

	def update(self):
		self.text()
		self.appendToArray()
		location.locationChange([['Watch the shore', Death, 'You sit among the wreckage of your once beautiful ship and reminisce about the old times. A shell rests in the sand next to you. You pick it up, examining the shell. Suddenly, you realize you are holding a cone snail. Before you can put the shell down and rectify your mistake, you are stabbed. Death is instant and painless.', False], ['Walk the path in front of you', GnarledPath, '', False]])

WreckedShore = WreckedShore()

class GnarledPath(location.Location):
	def __init__(self):
		location.Location.__init__(self, "Abandoned Shoals", "The Gnarled Path", "You start walking towards the path, when you stop in disbelief. An old wizened man with a long, gnarled cane is staring back at you. He motions that you should join him,but you are wary. You finish walking along the beach to the beginning of the path.")

	def update(self):
		self.text()
		self.appendToArray()
		location.locationChange([['Talk to the old man', oldMan, "", True], ['Continue along the path', RockyBase, "", False]])
	
GnarledPath = GnarledPath()
# "When you return the old man is still waiting, leaning on his cane. He gives you a wry grin, as if he knows something about you that you don't."
class SteepAscent(location.Location):
	def __init__(self):
		location.Location.__init__(self, "Abandoned Shoals", "The Steep Ascent", "You start your ascent of the seemingly insurmountable hill.")
		self.arr = ["The sun is setting fast in the distance.", "What if you throw yourself off? Would it really hurt that much?", "You miss your crew, especially your dog, Wilson.","You climb", "You climb","You climb.", "You climb.", "A mosquito lands on your arm. You smack it before it can bite you. You continue to climb.", "You contemplate life.", "Why would you even trust an old man? You consider turning back.", "A hare hops past, causing you to lose your balance.", "You stop for a second to catch your breath.", "A snake is in the middle of the path.", "You feel extremely dehydrated, and weary with life."] 
		self.ticker = 29
		self.progress = 'normal'
	def update(self):
		self.text()
		self.appendToArray()
		while globals.player.location == SteepAscent:
			randomInt = random.randint(1, 13)
			if randomInt == 10:
				self.progress = 'fall'
				print(self.arr[randomInt])
			elif randomInt == 12:
				self.progress = 'snake'
				print(self.arr[randomInt])
			elif randomInt == 1 or randomInt == 13:
				self.progress = 'death'
				print(self.arr[randomInt])
			elif randomInt == 9 or randomInt == 7 or randomInt == 2:
				self.progress ='reverse'
				print(self.arr[randomInt])
			else:
				self.progress = 'normal'
				print(self.arr[randomInt])
			if self.progress == 'normal':
				inp = input.inputLines(['Admit defeat and turn back', 'Keep on climbing'])
				if inp == 1:
					globals.player.location = RockyBase
				elif inp == 2:
					self.ticker += 1
			elif self.progress == 'fall':
				inp = input.inputLines(['Steady yourself', 'Fall off'])
				if inp == 1:
					self.ticker += 1
				elif inp == 2:
					print("You fall off. In the moments it takes for you to hit the ground, you regret trusting the old man.")
					globals.player.location = Death
			elif self.progress == 'reverse':
				inp = input.inputLines(['Keep on climbing', 'Turn back'])
				if inp == 2:
					globals.player.location == RockyBase
				elif inp == 1:
					self.ticker += 1
				elif type(inp) == str:
					return
			elif self.progress == 'snake':
				inp = input.inputLines(['Hit the snake with the stick', 'Inch around the snake'])
				if inp == 1:
					print("That was a stupid decision. The snake lunges at you, and sinks its fangs into your calf. The poison takes effect almost immediately, and you fall to the ground.")
					globals.player.location = Death
				elif inp == 2:
					self.ticker += 1
			elif self.progress == 'death':
				inp = input.inputLines(["Turn back", "Throw yourself off", "Climb some more"])
				if inp == 1:
					globals.player.location = RockyBase
				elif inp == 2:
					print("At this point, you don't care that you are dead.")
					globals.player.location = Death
				elif inp == 3:
					self.ticker += 1

			if self.ticker >= 30:
				globals.player.location = GrassyHill
				
SteepAscent = SteepAscent()

class RockyBase(location.Location):

	def __init__(self):
		location.Location.__init__(self, "Abandoned Shoals", "The Rocky Base", "You are at the bottom of a massive hill. You can see at the summit, a hill of grass. You stare up ahead at the top, your goal.")

	def update(self):
		self.onReturn(["Returning to the base was much easier than walking up it. You wonder if you were imagining how long it took to ascend the hill, then you shake off that thought.", GrassyHill])
		self.text()
		self.appendToArray()
		location.locationChange([["Go back to the shore", GnarledPath, "", False], ["Start climbing", SteepAscent, "", False]])

RockyBase = RockyBase()

class GrassyHill(location.HarvestLocation):

	def __init__(self):
		location.HarvestLocation.__init__(self, "Abandoned Shoals", "The Grassy Hill", "After a long and arduous climb, you finally reach the summit. You think to yourself: this would make a nice outpost.")
		self.maxHarvest = 15

	def update(self):
		self.text()
		self.appendToArray()
		if self.maxHarvest > 0:
			inp = input.inputLines(['Whack the grass', 'Go back down the hill'])
			if (inp == 1):
				self.maxHarvest -= globals.player.inventory.scavengeGrass(2, 4, self.maxHarvest, 5, ["Harvest grass", "Collect cut grass", "Scavenge for grass"],  ["Relax", "Sit down", "Do nothing", "Fall asleep", "Daydream", "Contemplate life", "Stop", "Watch a large, red beetle"])

			elif (inp == 2):
				globals.player.location = RockyBase
			elif type(inp) == str:
				return
		else:
			inp = input.inputLines(['Come back the way you came'])
			if (inp == 1):
				globals.player.location = RockyBase
			elif type(inp) == str:
				return

GrassyHill = GrassyHill()

class Death(location.Location):
	def __init__(self):
		location.Location.__init__(self, "", "Death", "Game Over")

	def update(self):
		self.text()
		self.appendToArray()
		globals.player.die()

Death = Death()



#CHANGE LOCATION START
globals.player.location = ForgottenShore
#CHANGE LOCATION START


globals.player.pLocation = GrassyHill
