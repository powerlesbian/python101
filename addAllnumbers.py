# extract out all the numbers in a file, line by line, and add them up

import re
handle=open('regex_sum_1846848.txt')
lst=list()
for line in handle:
    line =  line.rstrip()
    x=re.findall('[0-9]+',line)
    if x != []:
        for member in x:
            member=float(member)
            lst.append(member)

print(len(lst),lst)

answer01= sum(lst)
print(answer01)


