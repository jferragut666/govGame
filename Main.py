
from Land import Land
from Player import Player 
'''
import socket
# create all players and initialize land
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

while True:
	c, addr = s.accept()
	print "got connection from", addr
	c.send("thank you for connecting")
	c.close()
'''
jacob = Player("jacob",Land())
land = Land()
jacob = Player("jacob",land)
print jacob.getLand().getResources()
print jacob.getLand().getRegion()
jacob.setInventory("rock", 2)
print jacob.getInventory

