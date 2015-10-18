import checkouts
from player import Player

class Game:

	winner = None
	type = 501
	players = []

	def __init__(self):
		pass

	def setUp(self):
		print "Welcome to Bullseye! I'm your host, Jim."
		
		# What game are we playing?
		print "So what game would you like to play?"
		answer = int(raw_input())
		self.setType(answer)

		# How many players?
		print "How many players are there?"
		answer = int(raw_input())
		self.setPlayers(answer)
		return self

	def setPlayers(self, playerCount):
		players = []
		for i in range(1, playerCount + 1):
			print "Player %d what is your name?" % i
			name = raw_input()
			players.append(Player(name, self.type))
			print "Hello " + name
		self.players = players

	def setType(self, type):
		self.type = type

	def end(self):
		print "The Winner is %s" % self.winner.name
		print "Game Over."

	def hasWinner(self):
		if self.winner is not None:
			self.end()
			return True
		return False

	def hasOutshot(self, score):
		if str(score) in checkouts.checkouts():
			outshot = ''
			for shot in checkouts.checkouts()[str(score)]:
				outshot += shot + " "
			print "Outshot: %s" % outshot
		else:
			print "%d required" % score
