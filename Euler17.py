
num_dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 0:'zero',
			'and':'and', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
			16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 
			20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 
			'hundred':'hundred', 1000:'onethousand'}

for key in num_dict:
	length = len(num_dict[key])
	num_dict[key] = length

def total_letters(start, end):
	total = 0
	for i in range(start, end+1): # inclusive range
		if i <= 20 or i == 1000:
			total += num_dict[i]
		
		elif i < 100:
			if str(i)[-1] != '0':
				total += (num_dict[int(str(i)[0] + str(0))] + num_dict[int(str(i)[1])])
			else:
				total += num_dict[i]

		elif i < 1000:
			if str(i)[-2:] != '00':
				# Recursive case: recurses until base case is found in i <=20 or i < 100
				total += (num_dict[int(str(i)[0])] + num_dict['hundred'] + num_dict['and'] + total_letters(int(str(i)[1:]), int(str(i)[1:])))
			else:
				total += (num_dict[int(str(i)[0])] + num_dict['hundred'])
	return total

print total_letters(1, 1000)


