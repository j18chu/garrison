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
	'shorePath')

class Shore(location.Location):
	def __init__(self):
		location.Location.__init__(self, "shore", "coast", "The first thing you feel when you awake is a splitting headache. You slowly open your eyes, taking in the sand below you, the palm trees ringing your vision, and the small\ncrabs scuttling around you. You shut your eyes and massage your temples, trying to recall what happened. The last thing you remember was sailing the Blue Seas with your crew, being\nuniversally feared, and then the crash. You open your eyes up again, this time noticing the wreckage around you.\n")

	def update(self):
		input.printInput("The first thing you feel when you awake is a splitting headache. You slowly open your eyes, taking in the sand below you, the palm trees ringing your vision, and the small crabs scuttling around you. You shut your eyes and massage your temples, trying to recall what happened. The last thing you remember was sailing the Blue Seas with your crew, being universally feared, and then the crash. You open your eyes up again, this time noticing the wreckage around you.")
		location.locationChange([['Explore the wreckage', 'secondShore', ''], ['Close your eyes for a little longer', 'death', 'While you rest, a group of savages appear on the beach. Grotesquely dressed, they creep up on you. The one with the mask, clearly the leader, motions them towards you. No one hears your scream as they pummel you.']])

shore = Shore()

def secondShore():
	input.printInput('You walk around until you notice a plank of wood, larger than the rest. You turn it over and it reveals a name: The S.S. Furybringer. You finally remember who you were. You were a notorious captain who was as fearsome as he was cunning. You were able to recruit followers and pillage entire islands. You sigh, thinking about how all this is behind you. You notice a path ahead of you.')
	inp = input.inputLines(['Stay near the shore', 'Walk the path in front of you'])
	if (inp == 1):
		print("The tide slowly inches towards you. Out of nowhere, a giant shark eats you in one big gulp! You are dead.")
		globals.player.location = 'death'
	elif (inp == 2):
		globals.player.location = 'shorePath'
	elif type(inp) == str:
		return
	else:
		input.error(2)

def shorePath():
	input.printInput("You start walking towards the path, when you stop in disbelief. An old wizened man with a long, gnarled cane is staring back at you. He motions that you should join him,but you are wary. You finish walking along the beach to the beginning of the path.")
	inp = input.inputLines(['Talk to the old man', 'Continue along the path'])
	if (inp == 1):
		oldMan.openName()
	elif (inp == 2):
		globals.player.location = 'footOfHill'
	elif type(inp) == str:
		return
	else:
		input.error(2)
	
def climbHill():
	arr = ["The sun is setting fast in the distance.", "What if you throw yourself off? Would it really hurt that much?", "You miss your crew, especially your dog, Wilson.","You climb", "You climb","You climb.", "You climb.", "A mosquito lands on your arm. You smack it before it can bite you. You continue to climb.", "You contemplate life.", "Why would you even trust an old man? You consider turning back.", "A hare hops past, causing you to lose your balance.", "You stop for a second to catch your breath.", "A snake is in the middle of the path.", "You feel extremely dehydrated, and weary with life."]
	ticker = 30
	progress = 'normal'
	while globals.player.location == 'climbHill':
		randomInt = random.randint(1, 13)
		if randomInt == 10:
			progress = 'fall'
			print(arr[randomInt])
		elif randomInt == 12:
			progress = 'snake'
			print(arr[randomInt])
		elif randomInt == 1 or randomInt == 13:
			progress = 'death'
			print(arr[randomInt])
		elif randomInt == 9 or randomInt == 7 or randomInt == 2:
			progress ='reverse'
			print(arr[randomInt])
		else:
			progress = 'normal'
			print(arr[randomInt])
		if progress == 'normal':
			inp = input.inputLines(['Admit defeat and turn back', 'Keep on climbing'])
			if inp == 1:
				globals.player.location = 'footOfHill'
			elif inp == 2:
				ticker += 1
			else:
				input.error(2)
		elif progress == 'fall':
			inp = input.inputLines(['Steady yourself', 'Fall off'])
			if inp == 1:
				ticker += 1
			elif inp == 2:
				print("You fall off. In the moments it takes for you to hit the ground, you regret trusting the old man.")
				globals.player.location = 'death'
			elif type(inp) == str:
				return
			else:
				input.error(2)
		elif progress == 'reverse':
			inp = input.inputLines(['Keep on climbing', 'Turn back'])
			if inp == 2:
				globals.player.location == 'footOfHill'
			elif inp == 1:
				ticker += 1
			elif type(inp) == str:
				return
			else:
				input.error(2)
		elif progress == 'snake':
			inp = input.inputLines(['Hit the snake with the stick', 'Inch around the snake'])
			if inp == 1:
				print("That was a stupid decision. The snake lunges at you, and sinks its fangs into your calf. The poison takes effect almost immediately, and you fall to the ground.")
				globals.player.location = 'death'
			elif inp == 2:
				ticker += 1
			elif type(inp) == str:
				return
			else:
				input.error(2)
		elif progress == 'death':
			inp = input.inputLines(["Turn back", "Throw yourself off", "Climb some more"])
			if inp == 1:
				globals.player.location = 'footOfHill'
			elif inp == 2:
				print("At this point, you don't care that you are dead.")
				globals.player.location = 'death'
			elif inp == 3:
				ticker += 1
			elif type(inp) == str:
				return
			else:
				input.error(2)
		

		if ticker >= 30:
			globals.player.location = 'grassHill'
				

def footOfHill():
	input.printInput("You are at the bottom of a massive hill. You can see at the summit, a hill of grass.You stare up ahead at the top, your goal.")
	inp = input.inputLines(['Go back to the shore', 'Start climbing'])
	if (inp == 1):
		globals.player.location = 'shorePath'
	elif (inp == 2):
		globals.player.location = "climbHill"


	else:
		input.error(2)


def grassHill():
	input.printInput("After a long and arduous climb, you finally reach the summit. You think to yourself: this would make a nice outpost.")
	if len(globals.player.inventory.quests) == 1 and globals.player.inventory.grass < 16:
		inp = input.inputLines(['Whack the grass', 'Go back down the hill'])
		if (inp == 1):
			globals.player.inventory.scavengeGrass(2, 4, 15, 5, ["Harvest grass", "Collect it from the ground", "Scavenge for grass"],  ["Relax", "Sit down", "Do nothing", "Fall asleep", "Daydream", "Think about how many rest phrases I can come up with", "Contemplate life", "Stop", "Watch a large, red beetle"])

		elif (inp == 2):
			globals.player.location = 'footOfHill'
		elif type(inp) == str:
			return
		else:
			input.error(2)
	else:
		inp = input.inputLines(['Come back the way you came'])
		if (inp == 1):
			globals.player.location = 'footOfHill'
		elif type(inp) == str:
			return
		else:
			input.error(2)

	

def shoreStart(isStart):
	while isStart and globals.player.alive == True:
		if globals.player.location == 'firstShore':
			shore.update()
		elif globals.player.location == 'secondShore':
			secondShore()
		elif globals.player.location == 'shorePath':
			shorePath()
		elif globals.player.location == 'grassHill':
			grassHill()
		elif globals.player.location == 'footOfHill':
			footOfHill()
		elif globals.player.location == 'climbHill':
			climbHill()
		elif globals.player.location == 'death':
			globals.player.die()



shoreStart(True)