from src.player import Player
from src.game import Game

game = Game()
game.setUp()

while game.hasWinner() is False:
	for player in game.players:
		player.turn(game)
		if game.hasWinner() is True:
			break
		