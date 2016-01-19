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
			# add call to high_scores
			pass
		elif user_choice == "3":
			sys.exit()	



