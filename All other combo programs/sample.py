from bs4 import BeautifulSoup

import  requests

r= requests.get('https://www.cricbuzz.com/')



soup = BeautifulSoup(r.text, 'html.parser')

main = soup.find_all(id="match_menu_container")
first = main[0]

print(first.prettify())

