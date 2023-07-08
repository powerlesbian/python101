# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re


url = input('Enter webpage for extraction: ')
if url == '' :
    url = 'http://py4e-data.dr-chuck.net/comments_1846850.html'
html = urllib.request.urlopen(url).read()
#print (html)
numbers = re.findall(b'>([0-9]+)<', html)
#print(numbers)
count=0
sum=0
for num in numbers:
    count = count +1
    num= float(num.decode())
    sum = sum+ num
    print(count, num)

print ('the sum of numbers is', sum)