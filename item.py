import globals


class Item:

	def __init__(self, name, description, sell, buy, number = 1, equip = False):
		self.name = name
		self.description = description
		self.number = number
		self.sell = sell
		self.buy = buy
		self.usable = False

	def __str__(self):
		return self.name + ("" if self.number == 1 else ' (' + str(self.number) + ")")

	def allDescription(self):
		if self.description == "":
			return str(self)
		else:
			return self.name + ("" if self.number == 1 else '(' + str(self.number) + ")") + ": " + self.description

	def equal(self, item):
	    return item.name == self.name and item.description == self.description and item.sell == self.sell and item.buy == self.buy


	def stack(self, item):
		if self.equal(item):
			self.number += item.number
			return True
		else:
			return False

	def remove(self, num):
		if self.number >= num:
			self.number -= num
			return True
		else:
			return False

	def sell(self, amount):
		globals.player.inventory.addGold(self.sellCost * amount)
		globals.player.inventory.removeItem(self, amount)

	def buy(self, amount):
		if globals.player.inventory.removeGold(self.buy * amount):
			for i in range(len(amount)):
				globals.player.inventory.addItem(self)
			return True
		return False



class UsableItem(Item):

	def __init__(self, name, description, sell, buy, use, number = 1):
		Item.__init__(self, name, description, sell, buy, number)
		self.usable = True
		self.use = use

	def activate(self, user):
		user.inventory.removeItem(self)
		self.use(user)

class Nothing(Item):

	def __init__(self):
		Item.__init__(self, "nothing", "", 0, 0)

