#assignmt8-5
#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt


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
    print (words[1])
    lst.append(words[1])
print(len(lst),lst)

print("There were", len(lst), "lines in the file with From as the first word")