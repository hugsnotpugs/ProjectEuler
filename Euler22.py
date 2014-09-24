'''
What is the total of all name scores in the file?
1. Order names alphabetically
2. Calculate the letter scores
3. Namescore = Letter score * Name rank
'''

import os
os.chdir('/Users/chuanhe/desktop/code/Euler')

## Create a list of names
files = open('names.txt', 'r')
text = files.read() # this is is a string
text = text.split('","') # this is now a list of strings

# Clean out any leftover quotation marks
for i in range(len(text)):
	if text[i][0] == '"':
		text[i] = text[i][1:]
	elif text[i][-1] == '"':
		text[i] = text[i][:-1]	

# Sort the names
text = sorted(text)

# Initialize a dictionary of letter scores
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
letter_scores = {}
for i in range(len(letters)):
	letter_scores[letters[i]] = i + 1


# Calculate name scores for each and add to sum
total_score = 0

for i in range(len(text)):
	name_score = 0
	for letter in text[i]:
		name_score += letter_scores[letter]

	name_score = name_score * (i + 1)
	total_score += name_score

print total_score

