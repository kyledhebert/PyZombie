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
		turn_score = 0
		runners = 0
		while True:
			# show player hand
			print("You rolled:")
			for die in self.player.hand:
				print("[{}] {}".format(self.player.hand.index(die) + 1, die))
			# score brains rolled
				if die.value == "Brain":
					turn_score += 1
			# deduct health for shotguns rolled
				if die.value == "Shotgun":
					self.player.health -= 1
			# determine how many got away
				if die.value == "Runner":
					runners += 1
			# show the player the result of the roll		
			print("You have {} points so far".format(turn_score))
			print("You have {} hit points remaining".format(self.player.health))
			print("{} humans got away".format(runners))




			# ask player for action
			player_choice = input("[S]core Dice, [R]oll Again? ").lower()
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