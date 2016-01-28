import unittest

import dice, dice_cup, game, menu, player

class DiceCupTest(unittest.TestCase):
	"""Tests for the dice_cup module"""
	def setUp(self):
		self.cup = dice_cup.DiceCup()

	def test_for_six_green_die(self):
		self.assertTrue(self.cup.number_of_green_dice == 6)

	def test_for_four_yellow_die(self):
		self.assertTrue(self.cup.number_of_yellow_dice == 4)

	def test_for_three_red_dice(self):
		self.assertTrue(self.cup.number_of_red_dice == 3)

class PlayerTest(unittest.TestCase):
	"""Tests for the player module"""
	def setUp(self):
		self.cup = dice_cup.DiceCup()
		self.player = player.Player()
		self.player.add_dice_to_hand(self.cup)

	def test_for_three_dice_in_player_hand(self):
		self.assertTrue(len(self.player.hand) == 3)

"""
The GameTest don't run currently, since creating
a Game() instance actually launches the game, and 
expects user input.

TODO: seperate creation of a game object and 
playing the game
"""

# class GameTest(unittest.TestCase):
# 	"""Tests for the game module"""
# 	def setUp(self):
# 		self.game = game.Game()
# 		self.player = player.Player()
# 		self.computer = player.Player()
# 		self.player.turn_score = 3
# 		self.computer.turn_score = 3

# 	def test_scores_are_reset_at_start_of_round(self):
# 		self.game.start_round()
# 		self.assertTrue(self.player.turn_score == 0)
# 		self.assertTrue(self.computer.turn_score == 0)
		





				


if __name__ == '__main__':
	unittest.main()			