#! /usr/bin/env python3

# importing the libraries
from bs4 import BeautifulSoup
import requests

i=0
for i in range(58):

    url=f"https://ipv4.fetus.jp/ru?_lang=en-US&list-page={i}&cidr-page={i}"

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "html.parser")

    # print(soup.prettify())

    table = soup.find('tbody')
    table_rows = table.find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td] # saves values of inside an array 
        #print(row[0] + " | " + row[1] + " | " +  row[2] ) # print multiple rows
        print(row[0] )
        # create file
        with open("hello.txt", "a") as my_file:
            my_file.write(row[0])
            my_file.write("\n")