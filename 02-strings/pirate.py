english = ("sir", "hotel", "student", "boy", "madam", "professor", "restaurant", "your", 
	"excuse", "students", "are", "lawyer", "the", "restroom", "my", "hello", "is", "man")
pirate = ("matey", "fleabag inn", "swabbie", "matey", "proud beauty", "galley", "yer", "arr",
 "swabbies", "be", "foul blaggart", "th'", "head", "me", "avast", "be", "matey")

sentence = raw_input("""
	Create a sentence using some of the following words: sir, hotel, student, boy, madam, professor, 
	restaurant, your, excuse, students, are, lawyer, the, restroom, my, hello, is, man.\n""")
words = sentence.split(" ")
print words

for word in words:
	if word in english:
		i = english.index(word)
		print pirate[i],
	else:
		print word, 
		
