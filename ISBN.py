#  File: ISBN.py
#  Description: 
#  Student Name: Christina Hoang
#  Student UT EID: CH42297
#  Course Name: CS 303E
#  Unique Number: 518450
#  Date Created: 4/12/17
#  Date Last Modified: 4/15/17

# This function creates a new list of only numbers
# def isbn_list(lines):

def valid(isbn):
	isbn_list = isbn[::]
	isbn_list = list(isbn_list)
	isbn_list = [str(x) for x in isbn_list]
	accepted = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X", "x", "-"]
	new_isbn_list = ""
	for c in isbn_list:
		if c not in accepted:
			return False
		else:
			isbn_list.remove(c)
	if (len(new_isbn_list) == 0):
		return True

# This function calculates the partial sum
def partial_sum(n):
	n = [int(x) for x in n]
	s = []
	s = [int(x) for x in s]
	for i in range((len(n))):
		new_sum = 0
		if (i == 0):
			s.append(n[i])
		else:
			new_sum = s[i-1] + n[i]
			s.append(new_sum)
	return s

def main():
	# Open input and output files
	in_file = open("isbn.txt","r")
	out_file = open("isbnOut.txt","w")

	# Read lines in input file
	lines = in_file.readlines()

	for i in range(len(lines)):
		isbn = lines[i]

		# Test if ISBN code is valid
		if (valid(isbn) == False):
			output_line = isbn.strip("\n") + "	" + "invalid" 
			out_file.write(output_line)
			out_file.write("\n")

		else:
			# Create new list with only numbers from ISBN code
			new_isbn = []
			num_range = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
			num_count = 0
			for c in isbn:
				if (c == "X") or (c == "x"):
					new_isbn.append(10)
				elif (c in num_range):
					new_isbn.append(c)
					num_count += 1
				else:
					continue

			n = new_isbn

			# Determine validity of isbn

			# Calculate partial sum 1
			s1 = partial_sum(n)
			n = s1

			# Calculate partial sum 2
			s2 = partial_sum(n)

			# Write result to output file
			if (s2[-1] % 11 == 0):
				output_line = isbn.strip("\n") + "	" + "valid" 
				out_file.write(output_line)
				out_file.write("\n")
			else:
				output_line = isbn.strip("\n") + "	" + "invalid" 
				out_file.write(output_line)
				out_file.write("\n")
		
	# Close files
	in_file.close()
	out_file.close()
main()


