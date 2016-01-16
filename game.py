import random

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
		runners = 0
		self.player.add_dice_to_hand(self.dice_cup)
		while self.player.health > 0:
			# show player hand
			print("You rolled:")
			for die in self.player.hand:
				print(die)
			
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
				print("The score is Player: {}, Computer: {}"
					.format(self.player.score, self.computer.score))	
			# ask player for action
			elif not self.player_choice():
				break
			# resolve player turn
			# if player wins end game	
		


	# computer turn
	def computer_turn(self):
		runners = 0
		self.computer.add_dice_to_hand(self.dice_cup)
		while self.computer.health > 0:
			# show computer hand
			print("The computer rolled:")
			for die in self.computer.hand:
				print(die)

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

			# computer moves
			# the computer will always roll again if health >=2
			# if health = 1 will use random to decide to roll or not
			if self.computer.health >= 2:
				# remove brains and shotguns from hand
				for die in self.computer.hand:
					if die.value == "Brain" or die.value == "Shotgun":
						while die in self.computer.hand:
							self.computer.hand.remove(die)
					# reroll the dice still in hand 
						for die in self.computer.hand:
							die.roll_die()	
					# continue the computer's turn
					self.computer_turn()

			elif self.computer.health == 1:
				print("The computer has ended its turn")
				print("The score is Player: {}, Computer: {}"
					.format(self.player.score, self.computer.score))
				break
			elif self.computer.health <= 0:
				print("The computer has been killed")
				print("The score is Player: {}, Computer: {}"
					.format(self.player.score, self.computer.score))	



		# resolve computer turn
		# if computer wins end game

	# if no winners start next turn

	def player_choice(self):
		player_choice = input("[S]core Dice, [R]oll Again? ").lower()
		if player_choice in "sr":
			if player_choice == "s":
				self.player.score += self.player.turn_score
				print("The score is Player: {}, Computer: {}"
					.format(self.player.score, self.computer.score))
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


	def evaluate_hand(self, runners):
		"""Check the player's hand for Brain and Shotgun dice"""
		for die in self.player.hand:
			if die.value == "Brain":
				while die in self.player.hand:
					self.player.turn_score += 1
					self.player.hand.remove(die)
			elif die.value == "Shotgun":
				while die in self.player.hand:
					self.player.health -= 1
					self.player.hand.remove(die)
			elif die.value == "Runner":
				runners += 1
				die.roll_die()

				 				

	def __init__(self):
		self.setup()
		self.start_round()
		self.player_turn()
		self.computer_turn()



Game()