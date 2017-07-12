# 	File: CreditCard.py
#	Description: This program verifies a credit card number.
#	Student Name: Christina Hoang
#	Student UT EID: ch42297
#	Course Name: CS 303E
#	Unique Number: 518450
#	Date Created: 4/5/2017
#	Date Last Modified: 4/7/2017

# This function checks if a credit card number is valid
def is_valid(cc_num):
	odd_digit = 0
	cc_sum = 0
	cc_num.reverse()
	for i in range(len(cc_num)):
		if i % 2 == 0:
			cc_sum += cc_num[i]
		else:
			odd_digit = 2 * cc_num[i]
			cc_sum += (odd_digit % 10) + (odd_digit // 10) 
	return cc_sum


# This function returns the type of credit
def cc_type(CreditCard):
	if (CreditCard[0:2] == "34") or (CreditCard[0:2] == "37"):
		return ("Valid American Express credit card number")
	elif (CreditCard[0:4] == "6011") or (CreditCard[0:3] == "644") or (CreditCard[0:5] == "65"):
		return ("Valid Discover credit card number")
	elif (CreditCard[0:2] == "50") or (CreditCard[0:2] == "51") or (CreditCard[0:2] == "52") or (CreditCard[0:2] == "53") or (CreditCard[0:2] == "54") or (CreditCard[0:2] == "55"):
		return ("Valid MasterCard credit card number")
	elif (CreditCard[0] == "4"):
		return ("Valid Visa credt card number")
	else:
		return ("")

def main():
	CreditCard = str(input("Enter 15 or 16-digit credit card number: "))
	cc_num = [int(x) for x in CreditCard]
	
	# Check if credit card number is 15 or 16 digits
	if (len(cc_num) != 15) and (len(cc_num) != 16):
		print ("Not a 15 or 16-digit number")

	# Print type of credit card
	elif (is_valid(cc_num) % 10 == 0):
		print (cc_type(CreditCard))
	else:
		print ("Invalid credit card number")

main()