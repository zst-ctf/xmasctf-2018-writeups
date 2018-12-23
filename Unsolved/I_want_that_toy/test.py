#!/usr/bin/env python3

import requests
import base64

def get_output(text):
    encoded = base64.b64encode(text.encode()).decode()
    res = requests.get('http://199.247.6.180:10000/?toy=' + encoded)
    return res.text

print(get_output('A'*70))
