# 	File: DNA.py
#	Description: This program finds the longest matching sequences in DNA strand pairs.
#	Student Name: Christina Hoang
#	Student UT EID: ch42297
#	Course Name: CS 303E
#	Unique Number: 51845
#	Date Created: 3/26/2017
#	Date Last Modified: 3/28/2017

def main():
	#open file for reading
	in_file = open("dna.txt","r")
	
	print ("Longest Common Sequence")
	#read the number of pairs
	num_pairs = in_file.readline(1)
	num_pairs = num_pairs.strip()
	num_pairs = int(num_pairs)

	#read each pair of dna strand
	next(in_file)
	for i in range(num_pairs):
		st1 = str(in_file.readline())
		st2 = str(in_file.readline())
		st1 = str(st1.strip())
		st2 = str(st2.strip())
		st1.upper()
		st1.upper()	

		#order the strand by size
		if (len(st1) > len(st2)):
			dna1 = st1
			dna2 = st2
		else:
			dna1 = st2
			dna2 = st1

		#get all substrings of dna2
		wnd = len(dna2)
		long_strand = ""
		list_strand = []
		while (wnd > 1):
			start_idx = 0
			while ((start_idx + wnd) <= len(dna2)):
				sub_strand = dna2[start_idx:start_idx + wnd]
				if sub_strand in dna1:
					if len(sub_strand) > len(long_strand):
						long_strand = sub_strand
						list_strand.append(sub_strand)
					elif len(sub_strand) == len(long_strand):
						if sub_strand == long_strand:
							list_strand.append(sub_strand)
						else:
							list_strand.append(sub_strand)
				#move the window by one
				start_idx += 1
			#decrease the window size
			wnd = wnd - 1
			
		#print longest common sequence
		print("Pair", (i+1),": ", end = "")
		for z in range(len(list_strand)):
			if z == 0:
				print (list_strand[z])
			if z > 0:
				print("         ", end = "")
				print (list_strand[z])
		if len(list_strand) == 0:
			print ("No Common Sequence Found")

	#close file
	in_file.close()
main()