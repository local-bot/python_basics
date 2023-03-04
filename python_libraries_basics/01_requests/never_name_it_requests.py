#! /usr/bin/env python3

import requests
import json


url = "https://api.corona-zahlen.org/germany"
headers = {
    'User-agent'  : 'Sombrero Browser'
    }

r = requests.get(url, headers=headers)

json_response = r.json()['hospitalization']# evtl moch ['cases7Days] oder ähnliches dazu

print(json.dumps(json_response,indent=2)) # statt indennt, evtl. könntet man auch import pprint o.ä.
