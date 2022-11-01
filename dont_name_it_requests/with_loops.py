#! /usr/bin/env python3

import requests
import json


url = "https://api.corona-zahlen.org/germany/history/cases"
headers = {
    'User-agent'  : 'Sombrero Browser'
    }

r = requests.get(url, headers=headers)

json_data = r.json()

'''
json_data = r.json()['meta'] # filters meta
print(json.dumps(json_data, indent =2))
'''

# with loop
for cases in json_data:
    print(json.dumps(json_data['meta'], indent =2))

