
###############

# GET METHOD

from urllib import request, parse, error

fhand = request.urlopen('http://data.pr4e.org/romeo.txt')

fhandl = list(fhand)

content = [
    line.decode().strip()
    for line in fhandl
]

###############

# POST METHOD
from urllib.request import Request
import json


url = 'https://www.clientam.com/sso/Login'

data = {'Hello': 'World'}
data = json.dumps(data)
data = str(data)
data = data.encode('utf-8')

req =  Request(url, data=data)
resp = request.urlopen(req)

###############

from urllib.request import Request, urlopen


DATA = b'some data'
req = Request(url='http://localhost:8080', data=DATA, method='PUT')
with urlopen(req) as f:
    pass
print(f.status)
print(f.reason)

###############

#Use of Basic HTTP Authentication:

import urllib.request


# Create an OpenerDirector with support for Basic HTTP Authentication...
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='kadidd!ehopper')
opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib.request.install_opener(opener)
urllib.request.urlopen('http://www.example.com/login.html')


###############-

import urllib.request


req = urllib.request.Request('http://www.example.com/')
req.add_header('Referer', 'http://www.python.org/')
# Customize the default User-Agent header value:
req.add_header('User-Agent', 'urllib-example/0.1 (Contact: . . .)')
r = urllib.request.urlopen(req)


###############-

#Here is an example session that uses the GET method to retrieve a URL
# containing parameters:


import urllib.request
import urllib.parse

params = {'spam': 1, 'eggs': 2, 'bacon': 0}
params = urllib.parse.urlencode(params)
url = f"http://www.musi-cal.com/cgi-bin/query?{params}"
with urllib.request.urlopen(url) as f:
    print(f.read().decode('utf-8'))


###############-

import urllib.request
import urllib.parse


data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
data = data.encode('ascii')
with urllib.request.urlopen("http://requestb.in/xrbl82xr", data) as f:
    print(f.read().decode('utf-8'))