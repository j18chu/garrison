import globals

def intOrStr(var):
	try:
		return int(input(var))

	except:
		print('Please enter a number')
		

def printInput(array):
	for i in array:
		print(i)

def inputPrompt(prompt):
	return intOrStr(f"<{prompt}> ")

def addInt(upperBound, arrOfSuggestions):
	arr = []
	for i in range(1, upperBound+1):
		arr.append(f'{i}: {arrOfSuggestions[i-1]}')
	printInput(arr)

# Most important
def inputLines(arr):
	addInt(len(arr), arr)
	print(" ")
	output = inputPrompt("turn")
	globals.player.turn += 1
	printInput([" ", "______________________________________________________________________________________", f"										Turn {globals.player.turn}", ""])
	return output
# Most important

def error(int):
	print(f"Error: Please enter a value between 1 and {int}")

