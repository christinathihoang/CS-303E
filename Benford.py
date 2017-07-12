# 	File: Benford.oy
#	Description: This program verifies Benford's law for the US Census data of 2009.
#	Student Name: Christina Hoang
#	Student UT EID: ch42297
#	Course Name: CS 303E
#	Unique Number: 51845
#	Date Created: 4/27/2017
#	Date Last Modified: 4/29/2017

def main():
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['1'] = 0
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0
  pop_freq ['7'] = 0
  pop_freq ['8'] = 0
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()

  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = pop_data[-1]
    first_num = pop_num[0]
    nums += first_num
    # make entries in the dictionary
    if first_num in pop_freq:
    	pop_freq[first_num] += 1

  # close the file
  in_file.close()

  # find total count of numbers in dictionary
  total_count = 0
  for key, value in pop_freq.items():
  	total_count += value

  # calculate frequency and print results
  freq = 0
  print ("Digit".ljust(10), "Count".ljust(10), "%")
  for key, value in pop_freq.items():
  	freq = value/total_count * 100
  	print (str(key).ljust(10)	,str(value).ljust(10), round(freq,1),"%")
  
main()
