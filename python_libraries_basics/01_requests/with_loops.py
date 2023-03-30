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

'''
# the same but with for condition 
for cases in filtering_data_from_json:
    print(json.dumps(cases, indent=2 ))

looks like this:
  {
    "cases": 6344,
    "date": "2023-03-27T00:00:00.000Z"
  },
  {
    "cases": 4768,
    "date": "2023-03-28T00:00:00.000Z"
  },
  {
    "cases": 3025,
    "date": "2023-03-29T00:00:00.000Z"
  }
...

# filtering only date 
for cases in filtering_data_from_json:
    print(json.dumps(cases['date'], indent=2 ))

looks like this: 
"2023-03-15T00:00:00.000Z"
"2023-03-16T00:00:00.000Z"
"2023-03-17T00:00:00.000Z"
"2023-03-18T00:00:00.000Z"
"2023-03-19T00:00:00.000Z"
"2023-03-20T00:00:00.000Z"  
.....

'''