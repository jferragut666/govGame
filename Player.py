

class Player:
	playerList = []
	def __init__(self, playerName, land):
		Player.playerList.append(playerName)
		self.land = land 
		self.inventory = []	
	def getLand(self):
		return self.land		
	def getInventory(self):
		return self.inventory
	def setInventory(self, resource, num):
		self.inventory[resource] = num

