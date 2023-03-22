#! /usr/bin/env python3

# importing the libraries
from bs4 import BeautifulSoup
import requests

url="http://localhost"

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "html.parser")

# title = soup.find('title')

table = soup.find('tbody')
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row[0] + " | " + row[1] + " | " +  row[2] )

print(title.text)