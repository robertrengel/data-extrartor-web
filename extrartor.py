import csv
import requests
from bs4 import BeautifulSoup
from faker import Faker



url_api = "https://openlibrary.org/search/authors.json?q="
url_api_author = "https://openlibrary.org/authors/"
soup = ""
authors_codes = []
data_cvs = []
fake = Faker()

with open("parse.txt", "r",encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'html.parser')

authors = soup.select('.autor:not(.color-dark-gray.metas.hide-on-hover)')
titles = soup.find_all('h3')

list_of_authors = [author.get_text() for author in authors]
list_authors = list(set(list_of_authors))
list_of_titles = [title.get_text() for title in titles]

names_authors = [name.replace(' ', '%20') for name in list_authors]
# --> ---------------------------------------------------------------------

#print(names_authors)
for name in names_authors:
    response = requests.get(url_api + ''.join(name))
    data = response.json()
    key_author = data['docs'][0]['key']
    authors_codes.append(key_author)
#response = requests.get(url_api_author + key_author + ".json")
#data_author = response.json()
#print(key_author)
#print(data_author['birth_date'])


for author_key in authors_codes:

  response = requests.get(url_api_author + author_key + ".json")
  data = response.json()
  #birth_date = data['birth_date']
  birth_year = []
  death_year = []
  age = 0
  first_name = ""
  last_name = ""
  data_for_cvs = {}
  if "birth_date" in data:
    birth_date = data['birth_date']
    birth_year = birth_date.split()
    name = data['name'].split()
    if len(name) == 3:
      first_name = f"{name[0]} {name[1]}"
      last_name = name[2]
    elif len(name) == 2:
        first_name = name[0]
        last_name = name[1]
    elif len(name) == 1:
        first_name = name[0]
        last_name = ""

          #print(f"la fecha de nacimiento es: {birth_year[-1]}")
  else:
    birth_year = []
    #print("no hay fecha de nacimiento")

  if "death_date" in data and data['death_date']!= ")":
      death_date = data['death_date']
      death_year = death_date.split()
      #print(f"la fecha de muerte es: {death_year[-1]}")
  else:
      death_year = [2023]  
      #print("no 


  if death_year != [] and birth_year!= []:
      age = int(death_year[-1]) - int(birth_year[-1])
      #print(age)
  if age != 0 and first_name!= "" and last_name!= "":  
    data_for_cvs = {'firts_name': first_name, 'last_name': last_name, 'age': age, 'nationality': fake.country()}
    #print(data_for_cvs)
    data_cvs.append(data_for_cvs)
#print(data_cvs)

with open('authors.csv', 'w', newline='',encoding='utf-8') as archivo:
    campos = ['firts_name', 'last_name', 'age','nationality']
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    for dato in data_cvs:
        escritor.writerow(dato) 
