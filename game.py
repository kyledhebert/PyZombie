import random
import sys

from dice_cup import DiceCup
from player import Player
from dice import Die

class Game():
	def setup(self):
		self.dice_cup = DiceCup()
		self.player = Player()
		self.computer = Player()
	

	def start_round(self):
		self.player.turn_score = 0
		self.computer.turn_score = 0

			
	# player turn
	def player_turn(self):
		"""A single turn taken by the player"""
		runners = 0
		self.player.add_dice_to_hand(self.dice_cup)
			
		while self.player.health > 0:
			# show player hand
			print("\nYou rolled:\n")
			print("*" * 20)
			for die in self.player.hand:
				print(die)
			print("*" * 20 + "\n")	
			
			# evaluate hand
			for die in self.player.hand:
				if die.value == "Brain":
					self.player.turn_score += 1
					#self.player.hand.remove(die)
				elif die.value == "Shotgun":
					self.player.health -= 1
					#self.player.hand.remove(die)
				elif die.value == "Runner":
					runners += 1
					
			# show the player the result of the roll		
			print("You have {} points so far".format(self.player.turn_score))
			print("You have {} hit points remaining".format(self.player.health))
			print("{} humans got away".format(runners))

			if self.player.health <= 0:
				print("You have been killed")

				self.print_score()	
			# ask player for action
			elif not self.player_choice():
				break


	# computer turn
	def computer_turn(self):
		"""A single turn taken by the computer"""
		runners = 0
		self.computer.add_dice_to_hand(self.dice_cup)
		if not self.player_quit():

			while self.computer.health > 0:
				# show computer hand
				print("\nThe computer rolled:\n")
				print("*" * 20)
				for die in self.computer.hand:
					print(die)
				print("*" * 20)	
				# evaluate computer hand
				for die in self.computer.hand:
					if die.value == "Brain":
						self.computer.turn_score += 1
						#self.player.hand.remove(die)
					elif die.value == "Shotgun":
						self.computer.health -= 1
						#self.player.hand.remove(die)
					elif die.value == "Runner":
						runners += 1

				# show the result of the computer's roll
				print("The computer has {} points so far".format(self.computer.turn_score))
				print("They have {} hit points remaining".format(self.computer.health))
				print("{} humans got away".format(runners))

				if self.computer.health <= 0:
					print("The computer was killed")
					self.print_score()
				# computer decides to score or roll
				elif not self.computer_choice():
					break				


	def player_quit(self):
		"""Presents the player with a choice to continue or quit game"""
		# this is to break up the turns, since computer turns
		# happen so quickly, it can be hard to tell what is
		# happening
		player_choice = input("\n[C]ontinue or [Q]uit? ").lower()
		if player_choice in "cq":
			if player_choice == "q":
				print("Thanks for playing!")
				sys.exit()
			elif player_choice == "c":
					return False


	def player_choice(self):
		"""Presents player choice menu and resolves choice"""
		player_choice = input("\n[S]core Dice, [R]oll Again? ").lower()
		if player_choice in "sr":
			if player_choice == "s":
				self.player.score += self.player.turn_score
				self.print_score()
				return False
			elif player_choice == "r":
				# remove brains and shotguns from hand
				for die in self.player.hand:
					if die.value == "Brain" or die.value == "Shotgun":
						while die in self.player.hand:
							self.player.hand.remove(die)
				# reroll the runner dice still in the hand
				for die in self.player.hand:
					die.roll_die()
				# continue the player's turn	
				self.player_turn()
		else:
			return self.player_choice()		
				
			
	def computer_choice(self):
		"""Resolves the computer choice"""
		# the computer will always roll again if health >=2
		# if health = 1 computer will score dice
		# TODO randomize computer choice when health = 1
		if self.computer.health == 1:
			self.computer.score += self.computer.turn_score
			print("The computer has ended its turn")
			self.print_score()
			return False
		elif self.computer.health >= 2:
			for die in self.computer.hand:
				if die.value == "Brain" or die.value == "Shotgun":
					while die in self.computer.hand:
						self.computer.hand.remove(die)
			for die in self.computer.hand:
				die.roll_die()
			self.computer_turn()					


	def print_score(self):
		"""Prints the game score"""
		print("\nThe score is Player: {}, Computer: {}\n"
					.format(self.player.score, self.computer.score))

				
	def clean_up(self):
		"""Performs maintenance tasks between turns"""
		# create a new DiceCup to simulate
		# putting rolled die back in the cup
		self.dice_cup = DiceCup()
		# reset the player's health to full
		self.player.health = 3
		self.computer.health = 3



	def keep_playing(self):
		"""Determines if the game has been won"""
		if self.player.score >= 13 or self.computer.score >= 13:
			return False
		else:
			return True
				

	def __init__(self):
		self.setup()	
		while self.keep_playing():
			self.start_round()
			self.player_turn()
			self.clean_up()
			self.computer_turn()
			self.clean_up()

		if self.player.score > self.computer.score:
			print("You win!")
		elif self.player.score < self.computer.score:
			print("The computer won.")
				

					



Game()