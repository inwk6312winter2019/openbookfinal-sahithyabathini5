file1= open('Book1.txt','r')
file1=file1.readlines()
def character_word_count(file):
    hist=dict()
    for line in file:
        line=line.lower()
        line=line.strip()
        line=line.split()
        for word in line:
            if word not in hist:
                hist[word]=1
            else:
                hist[word]+=1
    print(hist)

    
    
    
    
    
    """""""""task1.5""""
    file=open("Book3.txt")
def starts_with_vow(file):
	t=("a", "e", "i", "o", "u")
	count=0
	for line in file:
		for word in line:
			if word[0] in t:
				count=count+1
	return count
print(starts_with_vow(file))
