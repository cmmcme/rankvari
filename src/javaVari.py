import requests
import re
from bs4 import BeautifulSoup


def FindName(matchString, text) :
    pattern = re.compile(matchString + '\s([a-zA-Z0-9]+)')
    ret = pattern.findall(text)
    return set(ret)


matchString = "class"
res = requests.get('https://raw.githubusercontent.com/cmmcme/testJava/master/Hi.java')
soup = BeautifulSoup(res.text, 'lxml')
soup_string = str(soup)

classnameSet = FindName(matchString, soup_string)

for i in classnameSet:
    print(i, ' ')
