import globals


def printInput(str):
	width = 150
	line = ""
	currentWord = 0
	arr = str.split()
	while currentWord < len(arr):
		if len(arr[currentWord]) + len(line) > width:
			print(line)
			line = ""
		line += arr[currentWord] + " "
		currentWord += 1
	if len(line) > 0:
		print(line)
	print(" ")

def intOrStr(var):
	try:
		return int(input(var))

	except:
		print('\nPlease enter a number\n')
		
def locationInLine():
	string = globals.player.location
	print(string)

def inputPrompt(prompt):
	var = intOrStr(f"<{prompt}> ")
	while type(var) != int:
		var = intOrStr(f"<{prompt}> ")
	return var


def addInt(arrOfSuggestions, map):
	for i in range(len(arrOfSuggestions)):		
		print (f'{i + 1}: {map(arrOfSuggestions[i])}')

# Most important
def inputLines(arr, map = lambda obj: str(obj)):
	addInt(arr, map)
	print(" ")
	output = inputPrompt("turn")
	
	while output > len(arr):
		print(f"\nPlease enter a number between 1 and {len(arr)}.\n")
		output = inputPrompt("turn")
	globals.player.turn += 1
	print(" ")
	print('_' * 86)
	print(f' 										Turn {globals.player.turn} \n')
	return output
# Most important