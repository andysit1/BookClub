import json
from os import remove
from urllib import response
import urllib.request
from attr import dataclass
from torch import zero_
import requests

import time

title = 'Harry Potter'

def r_scrap(data):
    data = data.replace(" ", "%20")
    source = requests.get('https://www.googleapis.com/books/v1/volumes?q='+data)
    info = source.json()
    return info

def r_id_scrap(pk):
    data = {}
    source = requests.get('https://www.googleapis.com/books/v1/volumes/'+pk)
    info = source.json()
    data = info['volumeInfo']
    f = open('data.txt', 'w')
    v = json.dumps(data, skipkeys=True)
    f.write(v)
    f.close()

def get_data(fname):
    f = open(fname+'.txt', 'r')
    contxt = f.readlines()
    d = json.loads(contxt[0])
    return d


#found this from... https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
def html_cleaned_data(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
