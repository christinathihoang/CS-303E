#  File: GuessingGame.py

#  Description: This program guesses a number between 1 and 100 inclusive through binary search.

#  Student Name: Christina HOang

#  Student UT EID: CH42297

#  Course Name: CS 303E

#  Unique Number: 51845

#  Date Created: 4/10/2017

#  Date Last Modified: 4/12/2017

# This function returns the mid number
def return_mid(lo, hi, mid, ans):
	if (ans == 1):
		return (lo + hi) // 2
	else:
		return (lo + hi) // 2

def main():
	print ("Think of a number between between 1 and 100 inclusive.")
	print ("And I will guess what it is in 7 tries or less.")

	# Ask if user is ready
	ready = str(input("Are you ready? (y/n): "))

	while (ready != "y") and (ready != "n"):
		ready = str(input("Are you ready? (y/n): "))

	# Use binary search to determine number 
	if (ready == "y"):
		lo = 0
		hi = 100
		mid = 50
		for number in range (1,8):

			# Check guess against number
			print ("Guess", number, ": The number you thought was", mid)
			ans = eval(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))

			# Generate new guess
			if (ans == 0):
				print ("Thank you for playing the Guessing Game")
				break
			elif (ans == 1):
				hi = mid
				mid = return_mid(lo, hi, mid, ans)
			elif (ans == -1):
				lo = mid
				mid = return_mid(lo, hi, mid, ans)

		# print result if number is not in range 1 - 100 inclusive
		if (ans != 0):
			print ("Either you guessed a number out of range or you had an incorrect entry.")
	else:	
		print ("Bye")
main()
