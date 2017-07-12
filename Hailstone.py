# File: Hailstone.py
# Description: This file determines which number in a range has the Hailstone sequence with the longest cycle length.
# Student Name: Christina Hoang
# Student UT EID: ch42297
# Course Name: CS 303E
# Unique Number: 51845
# Date Created: 3/1/2017
# Date Last Modified: 3/4/2017

def main():
	#prompt user to enter starting and ending number
	start_num = int(input("Enter starting number of the range: "))
	end_num = int(input("Enter ending number of the range: "))
	while (start_num < 0) or (end_num < 0) or (start_num > end_num):
		start_num = int(input("Enter starting number of the range: "))
		end_num = int(input("Enter ending number of the range: "))

	#calculate cycle length for each number
	longest_cycle = 0
	longest_num = 0
	for i in range (start_num, end_num+1):
		num = i
		cycles = 0
		while (i > 1):
			if (i % 2 == 0):
				i = i // 2
				cycles += 1
			else:
				i = i * 3 + 1
				cycles += 1
	#compare to find the longest cycle
		if (cycles > longest_cycle):
			longest_cycle = cycles 
			longest_num = num

	#print result
	print ("The number",longest_num,"has the longest cycle length of",longest_cycle)
main()
