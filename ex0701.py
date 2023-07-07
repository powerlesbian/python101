#ex0701

fileHandle = open('mbox-short.txt')
for lx in fileHandle:
    print(lx.rstrip().upper())