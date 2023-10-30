#######################open funkcija################### scrapeinimas

# filename =open("text.txt", "w")
#
# arba
# irasyti faila
# with open("text.txt", "w") as f:
#     content = f.write("hello world")
#
# skaityti faila
# with open("text.txt", "r") as f:
#     content = f.read()
# print(content)

# arba skaityti faila su sita komanda:

# filename = open("text.txt", "r")
# filename.read()
# print(filename)

# updatint faila su sita komanda:
#
# with open("text.txt", "a") as f:
#     content = f.write("\nDar viena eilute")


import requests
from bs4 import BeautifulSoup
import psycopg2

#kodai: 200-OK; 301-302 - File found / redirect; 403 - forbidden; 404 - not found; 500 Server error.

# url = "https://aruodas.lt"
# response = requests.get(url)
# print(response.status_code)
# print(response.content)


#Gauti duomenis is website!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# url = "https://aruodas.lt"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
#
# content_block = soup.find('div', class_= "top-three-adverts__wrapper").text.strip()
#
# print(content_block)



url = "https://aruodas.lt"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


content_block = soup.find_all('div', class_="top-three-adverts__wrapper")

# print(content_block)

flats_data = []

for content in content_block:
    flat_title = content.find("div", class_="top-three-adverts__advert__address").text.strip()
    flat_price = content.find("span", class_="top-three-adverts__advert__price__price").text.strip()

    flats_data.append((flat_title, flat_price))

print(flats_data)

###########################################################################
flats_data = []
def create_and_insert_flats():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="aruodas_informacija",
        user="postgres",
        password="Trepsi4batai!"
    )

    cursor = connection.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS aruodas_top (
            id SERIAL primary key,
            flat_title VARCHAR(300),
            flat_price DECIMAL(10,2)
            )
    """

    cursor.execute(create_table_query)
print("table created successfully!!!")






    url = "https://aruodas.lt"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")


    content_block = soup.select('div.top-three-adverts__wrapper div')


    for content in content_block:
        try:
            flat_title = content.find("div", class_="top-three-adverts__advert__address").text.strip()
            flat_price = content.find("span", class_="top-three-adverts__advert__price__price").text.strip()

            print(flat_title, flat_price)
            flats_data.append((flat_title, flat_price))

        except AttributeError:
            continue
    connection.commit()

create_and_insert_flats()
