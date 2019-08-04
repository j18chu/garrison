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
		print('Please enter a number')
		
def inputPrompt(prompt):
	return intOrStr(f"<{prompt}> ")

def addInt(arrOfSuggestions, map):
	for i in range(len(arrOfSuggestions)):		
		print (f'{i + 1}: {map(arrOfSuggestions[i])}')

# Most important
def inputLines(arr, map = lambda obj: str(obj)):
	addInt(arr, map)
	print(" ")
	output = inputPrompt("turn")
	globals.player.turn += 1
	print(" ")
	print('_' * 86)
	print(f' 										Turn {globals.player.turn} \n')
	return output
# Most important

def error(int):
	print(f"Error: Please enter a value between 1 and {int}")

