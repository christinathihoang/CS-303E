# 	File: Deal.py
#	Description: This file calculates the probability of winning at "Let's Make a Deal!"
#	Student Name: Christina Hoang
#	Student UT EID: ch42297
#	Course Name: CS 303E
#	Unique Number: 51845
#	Date Created: 2/26/2017
#	Date Last Modified: 2/28/2017

import random
def main():
	#prompt user to enter number of times he/she wants to play
	play = int(input("Enter number of times you want to play: "))

	win_switch = 0
	games = 1
	print ("Prize".center(10)+"Guess".center(10)+"View".center(10)+"New Guess".center(10))

	#assign numbers to each door
	while (games <= play):
		prize = str(random.randint(1,3))
		guess = str(random.randint(1,3))
		view = str(random.randint(1,3))
		while (guess == prize):
			guess = str(random.randint(1,3))
			view = str(random.randint(1,3))
		while ((view == prize) or (view == guess)):
			view = str(random.randint(1,3))
		#determine the door the contestant chooses when he changes his mind
		newguess = str(random.randint(1,3))
		while (newguess == guess) or (newguess == view):
			newguess = str(random.randint(1,3))
			#calculate number of wins
			if (newguess == prize):
				win_switch += 1
		print (prize.center(10)+guess.center(10)+view.center(10)+newguess.center(10))
		games += 1

	#calculate probability for winning
	switched_probability = win_switch/games
	notswitched_probability = 1 - switched_probability

	#print the results
	print ("Probability of winning if you switch = "+str(switched_probability))
	print ("Probability of winning if you do not switch = "+str(notswitched_probability))
main()