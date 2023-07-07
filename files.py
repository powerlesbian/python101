#files 
fname= input('Please enter the file name: ')
try:
    someFile = open (fname)
except:
    print('File cannot be opened:',fname)
    quit()
#counting number of lines that start with subject
#count=0
#for line in someFile:
    if line.startswith('Subject:'):
        count = count +1
#print('There were/was', count,'subject lines in',fname)
#for eachIteration in someFile:
    print (eachIteration)

foxtrot= someFile.read()
#striping extra return lines from output
#someFile = open('blabla.txt')
#for line in someFile:
#    line=line.rstrip()
#    if line.startswith('From:'):
#        print(line)

shouting=foxtrot.upper()
print(shouting.rstrip())
