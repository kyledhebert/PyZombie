import random

from dice_cup import DiceCup
from player import Player
from dice import Die

class Game():
	def setup(self):
		self.dice_cup = DiceCup()


	# player turn
	def player_turn(self):
		self.player = Player()
		self.add_dice_to_hand()
		# show player hand
		for die in self.player.hand:
			print(die)
		# ask player for action
		player_choice = input("[S]top, [R]oll Again? ").lower()
		# resolve player turn
		# if player wins end game	

	# computer turn
		# show computer hand
		# computer moves
		# resolve computer turn
		# if computer wins end game

	# if no winners start next turn

	def add_dice_to_hand(self):
		"""Adds dice to the current player's hand"""
		while len(self.player.hand) < 3:
			self.player.hand.append(self.dice_cup.dice_in_cup.
				pop(random.randint(0,(len(self.dice_cup.dice_in_cup) -1 ))))

	def __init__(self):
		self.setup()
		self.player_turn()


Game()