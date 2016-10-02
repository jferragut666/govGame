from random import shuffle

class Land:

	region = ["plains", "mountain", "tundra", "forest", "island"]
		
	
	def __init__(self):
		shuffle(Land.region)
		self.region = Land.region.pop()	
		self.resources = {"rocks":0,"ore":0,"lumber":0,"oil":0,"wheat":0}
	
	def getResources(self):
		return self.resources
		
	def getRegion(self):
		return self.region
