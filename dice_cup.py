import random

from dice import GreenDie, YellowDie, RedDie


class DiceCup():
	number_of_green_dice = 0
	number_of_yellow_dice = 0
	number_of_red_dice = 0
	dice_in_cup = []

	def fill_cup(self):
		"""Fills the cup with thirteen dice"""
		while self.number_of_green_dice < 6:
			self.dice_in_cup.append(GreenDie())
			self.number_of_green_dice +=1
		while self.number_of_yellow_dice < 4:
			self.dice_in_cup.append(YellowDie())
			self.number_of_yellow_dice += 1
		while self.number_of_red_dice < 3:
			self.dice_in_cup.append(RedDie())
			self.number_of_red_dice +=1


	def empty_cup(self):
		"""Empties the cup of all dice"""
		dice_in_cup = []		

	def __init__(self):
		number_of_green_dice = 0
		number_of_yellow_dice = 0
		number_of_red_dice = 0
		dice_in_cup = self.fill_cup()		


						


