import json
from urllib import response
import urllib.request

from torch import zero_

import requests

title = 'Harry Potter'

def r_scrap(data):
    data = data.replace(" ", "%20")
    source = requests.get('https://www.googleapis.com/books/v1/volumes?q='+data)
    info = source.json()
    return info



def r_id_scrap(pk):
    source = requests.get('https://www.googleapis.com/books/v1/volumes/'+pk)
    info = source.json()
    return info

