def main ():
	# Open the file
	in_file = open ("grid.txt", "r")

	# Read the dimension of the grid
	dim = in_file.readline ()
	dim = dim.strip ()
	dim = int (dim)

	# Create an empty grid
	grid = []

	# Populate the grid
	for i in range (dim):
		line = in_file.readline ()
		line = line.strip ()
		row = line.split ()
		for j in range (dim):
			row[j] = int (row[j])
			grid.append (row[j])
	# Print the grid
	print (grid)

	# Read each row in blocks of four 
	for row in grid:
		for i in range (dim - 3):
			prod = 1
			for j in range (i, i + 4):
				prod = prod * row[j]
			print (prod, end = " ")
	print ()

	# Read each column in blocks of four
	for j in range (dim):
		for i in range (dim - 3):
			for k in range (i, i + 4):
				print (grid[k][j], end = " ")
			print (end = " ")
	print ()

	# Go along all diagonals L to R in blocks of 4
	for i in range (dim - 3):
		for j in range (dim - 3):
			for k in range (4):
				print (grid[i + k][j + k], end = " ")
			print (end = "	")
		print ()

	# Go along all diagonals R to L in blocks of 4
	for i in range (dim - 3):
		for j in range (3, dim):
			for k in range (4):
				print (grid [i + k][j - k], end = " ")
			print (end = " ")
	print ()

		
main ()