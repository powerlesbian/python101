
#fname = input("Enter file name: ")
handle= open('mbox-short.txt')
#count = 0
lst=list()
for line in handle:
    line = line.rstrip()
    words = line.split()
    #insert Guardian compound statement to prevent traceback on lines with less than 3 word then checks for 'From' starting (order of or is important)
    if len(words) < 3 or words[0] != 'From':
        continue
#    print (words[1])
    lst.append(words[1])
#print(len(lst),lst)

counts = dict()
for member in lst:
	counts[member]=counts.get(member,0)+1
        
inverse =[(value, key) for key, value in counts.items()]
print('reversing tuples way:',max(inverse)[1], max(counts.values()))

print('using .get way:',max(counts, key=counts.get))
        
def maxSender(counts):
    v= list(counts.values())
    k=list(counts.keys())
    return k[v.index(max(v))]

print ('writing a list function way:',maxSender(counts))