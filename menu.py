import json
import sys



CHOICES = ["\n[1] START GAME", "[2] STATS", "[3] RULES", "[4] QUIT"]

def display_choices():
	for choice in CHOICES:
		print(choice)



def user_choice():
	user_choice = str(input("Please make a selection "))
	if user_choice in "1234":
		if user_choice == "1":
			return True
		elif user_choice == "2":
			display_stats()
		elif user_choice == "3":
			display_rules()
		elif user_choice == "4":
			sys.exit()
				


def display_stats():
	"""Displays the stats stored in stats.txt"""
	try:
		stats_file = open("stats", "rt")
		json_stats = stats_file.read()
		stats_file.close()
		stats = json.loads(json_stats)
		print("\nTotal Wins: {}\nTotal Losses: {}"
			.format(stats["wins"], stats["losses"]))
	except ValueError:
		print("You haven't played any games yet")	


def display_rules():
	"""Displays the game rules to the player"""
	print("""
		\nMMMMMMM BRRAAIINNS
		\nOn your turn take three dice from the cup and roll them.
		\nEach one is a human victim. Red dice are the toughest.
		\nGreen are easiest, and Yellow are medium tough.

		\nThe dice have three symbols:

		\nBRAIN - You ate your victim's brain. These are worth one point
		\nif you survive.

		\nSHOTGUN - The victim fought back. These cost you one of your three
		\nhealth points.

		\nRUNNER - The victim escaped! You can choose to re-roll these
		\nagain along with new dice to bring the total back to three.

		\nIf you roll three shotguns your turn ends. Otherwise, you can 
		\nchoose to stop and score, or continue.

		\nIf you decide to STOP, score 1 for each Brain you have,
		\nand put all the dice back into the cup. It’s the computer's turn.

		\nIf you choose to KEEP GOING, leave all your Runners on the table. 
		\nUnless all three of your dice are Runners, take enough random new dice 
		\nfrom the cup to total three, and roll again. Whenever you roll, you will
		\nroll three dice at a time.

		\nAfter you take new dice, you can’t decide to stop . . . you have to roll.

		\nIf you ever lose all of your health by rolling three shotguns in a single
		\nturn, your turn ends and you score NOTHING.

		\nPlay until you or the computer scores 13 points.
		""")
