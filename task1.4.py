
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
