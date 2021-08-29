import requests

from bs4 import BeautifulSoup

word = input()
link = input()

r = requests.get(link)

soup = BeautifulSoup(r.content, "html.parser")

all_p = soup.find_all("p")

for paragraph in all_p:
    if word in paragraph.text:
        print(paragraph.text)
