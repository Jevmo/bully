import checkouts

class Player:

	tmpScore = None
	turnTotal = 0
	game = None

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def name(self):
		return self.name

	def updateScore(self):
		self.score -= self.turnTotal

	def turn(self, game):
		self.game = game
		self.resetTurnTotal()
		print "%s to throw, you have %d remaining" % (self.name, self.score)
		self.tmpScore = self.score
		
		for dart in range(1,4):
			self.throwDart(dart)

			if self.hasBust():
				return

			if self.hasWon():
				return

		print "%s scored %d" % (self.name, self.turnTotal)
		self.updateScore()

	def throwDart(self, dart):
		self.hasOutshot().setTurnTotal(self.getDartScore(dart))
		print "%d scored" % self.turnTotal

	def setTurnTotal(self, dartScore):
		self.turnTotal += dartScore

	def resetTurnTotal(self):
		""" Resets the players 3 dart turn to 0	"""
		self.turnTotal = 0

	def hasBust(self):
		if (self.tmpScore - self.turnTotal == 1) or (self.tmpScore - self.turnTotal < 0):
			print "%s you've bust!" % self.name
			return True

	def getDartScore(self, dart):
		"""Returns the score for the thrown dart
		
		Only returns a valid score
		Example:
			63 will invoke the while loop as 63 is impossible to score with 1 dart
		"""
		print "Enter dart %d score: " % dart
		score = int(raw_input())
		
		# Check to see dart score is less than or equal to 60
		while score > 60:
			print "Easy there Phil Taylor, you can't score more than 60! Try again"
			score = int(raw_input())

		return score

	def hasOutshot(self):
		if str(self.tmpScore) in checkouts.checkouts():
			outshot = ''
			for shot in checkouts.checkouts()[str(self.tmpScore)]:
				outshot += shot + " "
			print "Outshot: %s" % outshot
		else:
			print "%d required" % self.tmpScore

		return self

	def hasWon(self):
		if self.score - self.turnTotal == 0:
			self.game.winner = self
			return True

