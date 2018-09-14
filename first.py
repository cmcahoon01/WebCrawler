from urllib.request import urlopen
from collections import Counter
import re

def Most_Common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]

def search(link):
    print(link)

    try:
        f = urlopen(link)
        myfile = f.read()
        y=re.findall('"(http.+?)"',str(myfile))
        print(len(y))
        for item in y:
            domain=re.findall('//(.+?)/',item)
            if not re.search('w3',item) and not domain in sites:
                sites.append(domain)
                reter = search(item)
    except Exception as e:
        print("failed")

sites=[]

start = "https://en.wikipedia.org/wiki/Construction_of_Rockefeller_Center"

search(start)


print("done??")
