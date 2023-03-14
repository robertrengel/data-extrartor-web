import csv
import requests
from bs4 import BeautifulSoup
from faker import Faker

soup = ""
authors_codes = []
data_cvs = []
fake = Faker()

with open("parse.txt", "r",encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'html.parser')


titles = soup.find_all('h3')

list_of_titles = [title.get_text()[:40] for title in titles]

for id, i in enumerate(list_of_titles, start=1):

  data_books = {'id': id,
                'title': i,
                'release_date': fake.date_object().strftime('%Y-%m-%d'),
                'cover':fake.image_url(),
                'views':fake.random_int(min=10, max=100),
                'stock':fake.random_int(min=10, max=100),
                'category_id': fake.random_int(min=1, max=10)}
  print(data_books)
  data_cvs.append(data_books)

with open('books_data.csv', 'w', newline='',encoding='utf-8') as archivo:
    campos = ['id','title', 'release_date','cover', 'views','stock', 'category_id']
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    for dato in data_cvs:
        escritor.writerow(dato) 
print("archivo creado") 



