import random

from dice import GreenDie, YellowDie, RedDie


class DiceCup():
	list_of_dice = []
	number_of_green_dice = 0
	number_of_yellow_dice = 0
	number_of_red_dice = 0

	def fill_cup(self):
		"""Fills the cup with thirteen dice"""
		while number_of_green_dice < 6:
			list_of_dice.append(GreenDie())
			number_of_green_dice ++
		while number of number_of_yellow_dice < 4:
			list_of_dice.append(YellowDie())
			number_of_yellow_dice ++
		while number_of_red_dice < 3:
			list_of_dice.append(RedDie())
			number_of_red_dice ++

	def deal_die(self):
		"""Deals a single to a player"""
		return random.choice(list_of_dice) 				


