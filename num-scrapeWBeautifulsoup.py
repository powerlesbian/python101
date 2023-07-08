# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter webpage: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'
elif len(url) ==1:
    url = 'http://py4e-data.dr-chuck.net/comments_1846850.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all span tags
targets = soup('span')
count =0
nummies=0
#print(targets)
#print (match_object)

for tart in targets:
    count = count +1
    nummies= nummies+ int(tart.contents[0])
#    print (count, nummies)
#    tart= float(tart.decode())
#    sum = sum+ nummies
#    print(count, tart)

print ('The sum of numbers is', nummies)



