## Remember to keep "with" and the for loop WITHIN the function
def word_count(file_name): ## This can work on any file we want to read
	total_words = 0
	with open("data/sherlockholmes.txt", "r") as file_to_read: 
		for line in file_to_read:
			words = line.split(" ") ## Gets a list of all of the words
			total_words += len(words) ## Increase by number of words we have
		return total_words

file_name = "sherlockholmes.txt"
print(word_count(file_name))

