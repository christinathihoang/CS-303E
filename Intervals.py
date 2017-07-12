#  File: Intervals.py
#  Description: This file collapses overlapping intervals.
#  Student Name: Christina Hoang
#  Student UT EID: ch42297
#  Course Name: CS 303E
#  Unique Number: 51845
#  Date Created: 4/24/2017
#  Date Last Modified: 4/26/2017

def main():
  # Open file
  in_file = open("intervals.txt", "r")

  intervals = []
  collapsed_intervals = []

  # Create list of tuples
  for line in in_file:
    line = line.strip()
    line = line.split()
    line = (int(x) for x in line)
    line = tuple(line)
    intervals.append(line)

  # Sort list of tuples
  intervals = sorted(intervals)

  # Collapse overlapping tuples
  min_tuple = intervals[0][0]
  max_tuple = intervals[0][1]
 
  new_tuple = ()

  for i in range(len(intervals)):
    if (max_tuple >= intervals[i][0]) and (max_tuple < intervals[i][1]):
      max_tuple = intervals[i][1]
    elif (max_tuple < intervals[i][0]):
      new_tuple = (min_tuple, max_tuple)
      collapsed_intervals.append(new_tuple)
      min_tuple = intervals[i][0]
      max_tuple = intervals[i][1]

  for j in range(len(intervals)):
    if (max_tuple >= intervals[j][0]) and (max_tuple < intervals[j][1]):
      max_tuple = intervals[j][1]
    elif (min_tuple >= intervals[j][0]) and (min_tuple < intervals[j][1]):
      min_tuple = intervals[j][0]
      new_tuple = (min_tuple, max_tuple)
      collapsed_intervals.append(new_tuple)

  # Print results
  print ("Non-intersecting intervals:")
  for i in range(len(collapsed_intervals)):
    if collapsed_intervals[i] == collapsed_intervals[i-1]:
      continue
    else:
      print (collapsed_intervals[i])

  # Sort intervals by size
  def by_size(collapsed_intervals):
    return abs(collapsed_intervals[0] - collapsed_intervals[1])
  print ()
  print ("Non-Intersecting Intervals in order of size:")
  collapsed_sort = sorted(collapsed_intervals, key = by_size)
  for j in range(len(collapsed_sort)):
    print (collapsed_sort[j])

  # Close file
  in_file.close()

main ()
