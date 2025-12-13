import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/"

response = requests.get(url)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, "html.parser")

qoute_blocks = soup.find_all("article", class_="product_pod")

for qoute in qoute_blocks:
    name = qoute.find("h3").find("a")["title"]


print("Назва:", name)
print("-"*40)