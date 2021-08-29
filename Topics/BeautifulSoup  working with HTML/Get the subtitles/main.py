import requests

from bs4 import BeautifulSoup

subtitle = int(input())
link = input()

r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")

h2 = soup.find_all("h2")

print(h2[subtitle].text)
