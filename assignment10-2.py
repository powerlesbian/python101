#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time 

fname = input('Please enter file:')
if len(fname) <1 : fname = 'mbox-short.txt'
handle = open(fname)

lst=list()
for line in handle:
    line = line.rstrip()
    words = line.split()
    #insert Guardian compound statement to prevent traceback on lines with less than 3 word then checks for 'From' starting (order of or is important)
    if len(words) < 3 or words[0] != 'From':
        continue
    lst.append(words[5])
collins = dict()
for time in lst:
    hour=time[0:2]
    collins[hour]=collins.get(hour,0)+1 

##print out the sorted hour and times it occurs
#for key, value in sorted(collins.items()):
#    print(key, value)

#flip key value and sort by popularity

templist= list()
for key, value in collins.items():
    newTuples=(value, key)
    templist.append(newTuples)

#print('Flipped', templist)
#Sorted by popularity
templist= sorted(templist, reverse=True)

#print out line by line the top 5:
for value, key in templist[:5]:
    print(key, value)

