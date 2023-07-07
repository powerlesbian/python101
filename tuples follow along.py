#Tuples follow along

#video 9.2 code follow along
counts = dict()
names = ['a','b','c','d']
for name in names:
	if name not in counts: 
		counts[name]=1
	else:
		counts[name]=counts[name]+1
print (counts)

##########################################

#achieve the same by using 
counts = dict()
names = ['a','b','c','d']
for name in names:
	counts[name]=counts.get(name, 0)+1
print(counts)

#where name is the key, and 0 is the default value
#x takes on the value of name or 0 if key doesn’t exist
#####################################################

#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word]=counts.get(word,0)+1

lst = list()
for key, value in counts.items():
	newTup = (value, key)
	lst.append(newTup)
	
lst = sorted(lst, reverse=True)

for value, key in lst[:10]:
	break
#	print (key, value)


######### shorter version achieved with list comprehension to create a dynamic list

c= {'a': 10, 'b': 1, 'c': 22, 'd': 4}
#print(sorted([(v,k) for k,v in c.items()],reverse=True)) 

print(60*980.4, 29*735.3, 12*722.4)
print(58824.0+21323.699999999997+8668.8)
invTot= 76948.5
#print(dir(list))