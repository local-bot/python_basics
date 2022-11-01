#! /usr/bin/env python3

import requests
import json


url = "https://api.corona-zahlen.org/germany"
headers = {
    'User-agent'  : 'Sombrero Browser'
    }

r = requests.get(url, headers=headers)

json_response = r.json()['hospitalization']#  maybe also ['cases7Days] 

print(json.dumps(json_response,indent=2)) # indent=2 or pprint