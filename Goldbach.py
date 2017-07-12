# 	File: Goldbach.py
#	Description: This program verifies Goldbach's conjecture in a range of numbers.
#	Student Name: Christina Hoang
#	Student UT EID: ch42297
#	Course Name: CS 303E
#	Unique Number: 51845
#	Date Created: 3/22/2017
#	Date Last Modified: 3/24/2017

#determine if number is prime
def is_prime(n):
	limit = 0
	if (n == 1):
		return False
	limit = int(n ** 0.5) + 1
	divisor = 2
	while (divisor < limit):
		if (n % divisor == 0):
			return False
		divisor += 1
	return True

#generates list of even integers within input range
def find_even(lower, upper):
	nums = []
	even_num = 0
	while lower <= upper:
		nums.append(lower)
		lower += 2
	return (nums)

#generates list of primes within input range
def find_primes(max_num):
	n = 2
	list_prime = []
	while n < max_num:
		if is_prime(n) == True:
			list_prime.append(n)
		n += 1
	return list_prime

#verifies Goldbach conjecture
def test_Goldbach(n, list_prime):
	prime_sum = []
	for i in range(len(list_prime)):
		a = list_prime[i]
		for j in range(len(list_prime)):
			b = list_prime[j]
			total = a + b
			if a <= b:
				if total == n:
					prime_sum.append(a)
					prime_sum.append(b)
	return (prime_sum)

def main():
	#prompts user to enter a range of numbers
	lower = eval(input("Enter the lower limit: "))
	upper = eval(input("Enter the upper limit: "))

	#error checks on input range
	while (lower < 4) or ((lower%2) != 0) or ((upper%2) != 0) or (lower>upper):
		lower = eval(input("Enter the lower limit: "))
		upper = eval(input("Enter the upper limit: "))

	nums = find_even(lower,upper)
	max_num = max(nums)
	list_prime = find_primes(max_num)

	#print output
	for i in range(len(nums)):
		n = nums[i]
		prime_sum = test_Goldbach(n,list_prime)
		print("\n",n, end="")
		for z in range(len(prime_sum)-1):
			if (z%2) == 0:
				c = prime_sum[z]
				d = prime_sum[z+1]
				print(" =",str(c),"+",str(d), end="")
main()