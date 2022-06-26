import json
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



