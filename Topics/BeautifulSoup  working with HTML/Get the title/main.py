import requests

from bs4 import BeautifulSoup

link = input()

r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")

print(soup.find("h1").text)
