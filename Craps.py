# File: Craps.py
#	Description: This file calculates the probability of winning at Craps.
#	Student Name: Christina Hoang
#	Student UT EID: ch42297
#	Course Name: CS 303E
#	Unique Number: 51845
#	Date Created: 2/21/2017
#	Date Last Modified: 2/24/2017


import random
#simulate a single round of craps and return 1 if player wins and 0 if he loses
def craps(n):
  #come out roll
  x = random.randint(1,6)
  y = random.randint(1,6)
  total = x + y
  if (total == 7 or total == 11):
  	return 1
  if (total == 2 or total == 3 or total == 12):
  	return 0
  if (total == 4 or total == 5 or total == 6 or total == 8 or total == 9 or total == 10):
    #point roll
    j = 1
    while (j > 0):
      new_x = random.randint(1,6)
      new_y = random.randint(1,6)
      new_total = new_x + new_y
      if (new_total == total):
      	return 1
      if (new_total == 7):
      	return 0
      else:
      	j += 1
    n += 1

def main():
  #prompt the user to enter the number of rounds
  num_rounds = int(input("Enter the number of rounds: "))

  #compute the number of times he wins
  num_wins = 0
  for n in range (1, num_rounds+1):
  	num_wins += craps(n)
  	n += 1
  
  #print the result
  print ("Player wins", num_wins, "out of", num_rounds, "rounds.")
main ()