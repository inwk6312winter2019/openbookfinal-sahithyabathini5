def sorted_words(a):
	fin = open("Book3.txt",'r')
	for line in fin:
		word = line.strip()	
		print(word)
		word.sort()
sorted_words("Book3.txt")
