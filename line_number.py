with open("data/sherlockholmes.txt", "r") as sherlock_holmes_file:
	line_number = 0
	for line in sherlock_holmes_file:
		## Print the first 18 lines
		if line_number < 50:
			print(line)
		line_number += 1