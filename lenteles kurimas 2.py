import requests
from bs4 import BeautifulSoup
import psycopg2






url = "https://www.aruodas.lt/uzsienio-objektai/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


content_block = soup.find_all('div, class_=project-list-content div')

# print(content_block)

flats_data = []

for content in content_block:
    flat_title = content.find("h2", class_="project-title-full project-title").text.strip()
    flat_price = content.find("h3", class_="project-title-full project-min-values").text.strip()

    flats_data.append((flat_title, flat_price))

print(flats_data)
