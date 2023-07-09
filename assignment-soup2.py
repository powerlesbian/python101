# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def loopyScrape(link,count):

    url = link
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    #print(html)
    # Retrieve all of the anchor tags
    tags = soup('a')
    lst01= list()
    for tag in tags:
        lst01.append(tag.get('href', None))
    linknew= lst01[17]
    print(linknew)
    count = count +1
    if count > 6 :
        quit()
    else:
        loopyScrape(linknew, count)
    

loopyScrape('http://py4e-data.dr-chuck.net/known_by_Moayd.html',0)