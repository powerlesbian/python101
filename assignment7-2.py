#assignment7.2 count lines extract float and compute average
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count=0
total=0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count +1
        ipos = line.find(':')
        wanted=line[ipos+1:]
        wanted01=wanted.strip()
        print(wanted01)
        wanted02=float(wanted01)
        total = total+wanted02

#print('There were',count,'counts of X-DSPAM... in', fname)
#print('The total amount of extracted numbers is', total)
print('Average spam confidence:', total/count)


#print("Done")