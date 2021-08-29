import requests

from bs4 import BeautifulSoup

act = int(input())
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

a = soup.find_all("a")

print(a[act - 1].get("href"))
