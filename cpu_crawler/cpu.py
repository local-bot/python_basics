import re
import requests
from bs4 import BeautifulSoup

def print_logo():
        print("\n")
        print("############################################")
        print('#### Ebay-Kleinanzeigen CPU-Crwaler 1.0 ####')
        print("############################################")

print_logo()

# remove input(...) if you want to use this as a cronjob
base_url = "https://www.kleinanzeigen.de"
zu_suchen = input(f"\nCPU-Modell eingeben (Standard: ryzen 5600x): ") or "5600x"
min_price = input(f"Mindestpreis eingeben (Standard: 50): ") or "50"
max_price = input(f"Höchstpreis eingeben (Standard: 100): ") or "100"
ort = input(f"PLZ eingeben (Standard: 96050): ") or "96050"
entfernung = input(f"Entfernung in km eingeben (Standard: 300): ") or "300"
pls_exclude = "^(S|s)uche|\*(S|s)uche|SUCHE"

print(f"\nErgebnise für CPU {zu_suchen} werden gesucht ...\n")
print(f"PLZ: {ort}")
print(f"Entfernung: {entfernung} km")
print(f"Min Preis: {min_price} €")
print(f"Max Preis: {max_price} €")

search_url = f"https://www.kleinanzeigen.de/s-pc-zubehoer-software/prozessor_cpu/{ort}/preis:{min_price}:{max_price}/{zu_suchen}/k0c225l6891r{entfernung}+pc_zubehoer_software.art_s:prozessor_cpu"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'}

r = requests.get(search_url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
divisions = soup.find_all("div", {"class": "aditem-main--middle"}) # <div> = divisions
amount_results = 0


for data in divisions: # HTML Attributes -> https://www.w3schools.com/html/html_attributes.asp
        hyperlink = data.find_all("a") # <a> = hyperlinks

        article_title = hyperlink[0].text.strip() if hyperlink else "no title available"
        if re.search(pls_exclude, article_title):
                continue

        result_url = f"URL: {base_url}{hyperlink[0].get('href')}" if hyperlink else "no url available"

        # extract all <p> values
        paragraphs = data.find_all("p")

        price = paragraphs[1].text.strip() if len(paragraphs) > 1 else "no price available"
        # description = paragraphs[0].text.strip() if len(paragraphs) > 1 else "no description available" # add if needed

        print("\n------------------------------------------------------------------------------------------------------")
        print(f"\n{article_title} für {price} \n{result_url}")
        amount_results += 1

        with open("hello.txt", "a") as my_file:
                my_file.write("\n------------------------------------------------------------------------------------------------------\n")
                my_file.write(f"{article_title} für {price}\n{result_url}")
                my_file.write("\n------------------------------------------------------------------------------------------------------\n")
print("\n------------------------------------------------------------------------------------------------------\n")

if amount_results > 0:
        print(f"\tAnzahl der Ergebnise: {amount_results}")
        print("\tListe wurde als hello.txt gespeichert\n\n")
        # insert sendmail or send mss later here
else:
        print("keine Ergebnise gefunden :( \n\n")
        with open("hello.txt", "w") as my_file:
                my_file.write("Keine Ergebnise")
