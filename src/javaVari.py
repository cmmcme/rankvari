import requests
import re
from bs4 import BeautifulSoup


def FindName(url, matchString) :
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    text = str(soup)
    pattern = re.compile(matchString + '\s([a-zA-Z0-9]+)')
    ret = pattern.findall(text)
    return set(ret)


##res = requests.get('https://raw.githubusercontent.com/cmmcme/testJava/master/Hi.java')
##soup = BeautifulSoup(res.text, 'lxml')
## soup_string = str(soup)