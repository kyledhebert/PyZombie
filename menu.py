import json
import sys



CHOICES = ["\n[1] START GAME", "[2] STATS", "[3] QUIT"]

def display_choices():
	for choice in CHOICES:
		print(choice)



def user_choice():
	user_choice = str(input("Please make a selection "))
	if user_choice in "123":
		if user_choice == "1":
			return True
		elif user_choice == "2":
			display_stats()
		elif user_choice == "3":
			sys.exit()	


def display_stats():
	"""Displays the stats stored in stats.txt"""
	stats_file = open("stats", "rt")
	json_stats = stats_file.read()
	stats_file.close()
	stats = json.loads(json_stats)
	print("\nTotal Wins: {}\nTotal Losses: {}"
		.format(stats["wins"], stats["losses"]))

