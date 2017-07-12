#  File: Books.py
#  Description: This program analyzes the vocabulary in two novels.
#  Student Name: Christina Hoang
#  Student UT EID: CH42297
#  Course Name: CS 303E
#  Unique Number: 518450
#  Date Created: 5/1/2017
#  Date Last Modified: 5/5/17

# Create word dictionary from the comprehensive word list
word_dict = {}
def create_word_dict(word_list, word_dict):
	for word in word_list:
		word = word.strip()
		if word in word_dict:
			word_dict[word] += 1
		else:
			word_dict[word] = 1
	return word_dict

# Remove punctuation marks from a string
def parseString(st):
	new_st = ""
	for i in range(len(st)):
		if (st[i].isspace()):
			new_st += st[i]
		elif (st[i] == "'") and (st[i + 1] != "s"):
			new_st += st[i]
		elif (st[i] == "'") and ((st[i + 1] != "s") and (st[i + 1] != " ")):
			pass
		elif (st[i] == "s") and (st[i - 1] == "'"):
			pass
		elif (st[i].isalpha()):
			new_st += st[i]
	return new_st
	

# Returns a dictionary of words and their frequencies
def getWordFreq(file):
	book = open(file, "r")
	freq_dict = {}
	capital_dict = {}
	unique_dict = set()
	for st in book:
		new_st = parseString(st)
		new_st = new_st.split()
		for ch in new_st:
			if ch in freq_dict:
				freq_dict[ch] += 1
			else:
				freq_dict[ch] = 1
	for ch in freq_dict:
		if (ch[0] >= "A") and (ch[0] <= "Z"):
			capital_dict[ch] = freq_dict[ch]

	for capkey, capvalue in capital_dict.items():
		lower_cap = capkey.lower()
		if lower_cap in freq_dict:
			freq_dict[lower_cap] += capvalue
		elif lower_cap in word_dict:
			freq_dict[lower_cap] = capvalue
		else:
			unique_dict.add(capkey)
		del freq_dict[capkey]
	return (freq_dict)
	book.close()

# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
	distinct_words1 = len(freq1)
	total_words1 = 0
	for key1, value1 in freq1.items():
		total_words1 += value1
	percent1 = (distinct_words1/total_words1) * 100

	distinct_words2 = len(freq2)
	total_words2 = 0
	for key2, value2 in freq2.items():
		total_words2 += value2
	percent2 = (distinct_words2/total_words2) * 100
	
	set1 = set(freq1)
	set2 = set(freq2)
	diff1 = set1 - set2
	diff2 = set2 - set1
	count1 = 0
	for i in diff1:
		count1 += freq1[i]
	count2 = 0
	for i in diff2:
		count2 += freq2[i]
	rel_freq1 = (count1/total_words1) * 100
	rel_freq2 = (count2/total_words2) * 100

	print (author1)
	print ("Total distinct words =", distinct_words1)
	print ("Total words (including duplicates) = ", total_words1)
	print ("Ratio = ", percent1)
	print ()
	print (author2)
	print ("Total distinct words =", distinct_words2)
	print ("Total words (including duplicates) = ", total_words2)
	print ("Ratio = ", percent2)
	print ()
	print (author1, "used", len(diff1), "words that", author2, "did not use")
	print ("Relative frequency of words used by", author1, "not in common with", author2,"=", rel_freq1)
	print ()
	print (author2, "used", len(diff2), "words that", author1, "did not use")
	print ("Relative frequency of words used by", author2, "not in common with", author1,"=", rel_freq2)


def main():
	# Create word dictionary from comprehensive word list
	word_list = open("words.txt", "r")
	create_word_dict(word_list, word_dict)
	word_list.close()

	# Enter names of the two books in electronic form
	book1 = input("Enter name of first book: ")
	book2 = input("Enter name of second book: ")
	print()


	# Enter names of the two authors
	author1 = input("Enter last name of first author: ")
	author2 = input("Enter last name of second author: ")
	print()

	# Get the frequency of words used by the two authors
	freq1 = getWordFreq(book1)
	freq2 = getWordFreq(book2)

	# Compare the relative frequency of uncommon words used by the two authors
	wordComparison(author1, freq1, author2, freq2)
main()