import requests
from bs4 import BeautifulSoup

#Как получать запросы
# response = requests.get("https://httpbin.org/get")
# print(response.content)
# print()
# print(response.text)

#Как отправлять запрос
# response = requests.post("https://httpbin.org/post", data="Test data", headers = {"h1": "Test title"})
# print(response.text)


# response = requests.get("https://coinmarketcap.com/")
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith("$"):
#         for parse_elem_2 in parse_elem_1.split("</span>"):
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 print(parse_elem_2)


url = "http://quotes.toscrape.com/"

#Если что то не так то оно покажет ошибку
#----------------------------------
response = requests.get(url)
response.raise_for_status()
#----------------------------------
html = response.text

soup = BeautifulSoup(html, "html.parser")

qoute_blocks = soup.find_all("div", class_="quote")

for qoute in qoute_blocks:
    text = qoute.find("span", class_="text").text
    author = qoute.find("small", class_="author").text
    tags = [tag.text for tag in qoute.find_all("a", class_="tag")]

print("Цитата:",text)
print("Цитата:",author)
print("Цитата:",tags)
print("-"*40)