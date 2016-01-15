import random

class Die():
	color = ""
	list_of_values = []

	def __init__(self):
		self.value = random.choice(self.list_of_values)

	def __str__(self):
		return "{} Die, {}".format(self.color.title(),
							self.value.title())


class RedDie(Die):
	color = "Red"
	list_of_values = ["Brain", "Runner", "Runner", "Shotgun", "Shotgun", "Shotgun"]


class YellowDie(Die):
	color = "Yellow"
	list_of_values = ["Brain", "Brain", "Runner", "Runner", "Shotgun", "Shotgun"]


class GreenDie(Die):
	color = "Green"
	list_of_values = ["Brain", "Brain", "Brain", "Runner", "Runner", "Shotgun"]

			







