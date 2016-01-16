import random

from dice_cup import DiceCup



class Player():
	hand = []
	health = 3
	score = 0
	turn_score = 0


	def add_dice_to_hand(self, dice_cup):
		"""adds dice to the player's hand from the cup"""
		while len(self.hand) < 3:
			self.hand.append(dice_cup.dice_in_cup.
				pop(random.randint(0,(len(dice_cup.dice_in_cup) -1 ))))		



	
		






