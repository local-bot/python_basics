#! /usr/bin/env python3

import requests
import json


url = "https://api.corona-zahlen.org/germany/history/cases"


r = requests.get(url)

my_jason_request = r.json()
# my_jason_request = r.json()['meta'] # filters out meta
# my_jason_request = r.json()['data'] # filters out data

# fitlering out data 
filtering_data_from_json = my_jason_request['data']
print (json.dumps(filtering_data_from_json, indent=2))

# the same but with for condition 
'''
for cases in filtering_data_from_json:
    print(json.dumps(cases, indent=2 ))

'''

# filtering only date 
'''
for cases in filtering_data_from_json:
    print(json.dumps(cases['date'], indent=2 ))

'''