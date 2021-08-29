import requests

from bs4 import BeautifulSoup

link = input()

r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")

paragraphs = soup.find_all()
