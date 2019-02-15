f1= open('Book1.txt','r')
f2=open('book2.txt','r')
f3=open('book3.txt','r')
import operator
dict1=dict()
output=[]

def common_words(): 
  for line in f1:
    line=line.strip()
    line=line.lower()
    line=line.split()
    for word in line:
      if word not in dict1:
             dict1[word]=1
      elif word in dict1:
             dict1[word]+=1
  for line in f2:
    line=line.strip()
    line=line.lower()
    line=line.split()
    for word in line:
      if word not in dict1:
        dict1[word]=1
      elif word in dict1:
        dict1[word]+=1
  for line in f3:
    line=line.strip()
    line=line.lower()
    line=line.split()
    for word in line:
      if word not in dict1:
             dict1[word]=1
      elif word in dict1:
             dict1[word]+=1
  i=0
  while i<21:
    v=list(dict1.values())
    k=list(dict1.keys())
    if k[v.index(max(v))] not in output:
      output.append(k[v.index(max(v))])
    i+=1
  print(output)
common_words()
