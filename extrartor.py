import requests
from datetime import datetime
from bs4 import BeautifulSoup


names_authors = []
url = "https://www.buscalibre.pe/libros/ficcion/ciencia-ficcion"
url_api = "https://openlibrary.org/search/authors.json?q="

response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

authors = soup.select('.autor:not(.color-dark-gray.metas.hide-on-hover)')
titles = soup.find_all('h3')

list_of_authors = [author.get_text() for author in authors]
list_authors = list(set(list_of_authors))
list_of_titles = [title.get_text() for title in titles]

# --> create a list of all the names of the authors--------------------------
# for name in list_authors:
#     part = name.split()
#     if len(part) == 2:
#         names_authors.append({'name': part[0], 'last_name': part[1]})
#     elif len(part) == 3:
#         names_authors.append({'name': f'{part[0]} {part[1]}', 'last_name': part[2]})
#     else:
#         names_authors.append({'name': part[0], 'last_name': ''})
# --> ---------------------------------------------------------------------

# --> create a list with all space replaced by %20--------------------------

for name in list_authors:
    names_authors.append(name.replace(' ', '%20'))
    
# --> ---------------------------------------------------------------------

# print(names_authors)

response = requests.get(url_api + ''.join(names_authors[2]))

data = response.json()
name = data['docs'][0]['name']
fecha = []

if "birth_date" in data['docs'][0]:
    birth_date = data['docs'][0]['birth_date']
    fecha = birth_date.split()
    print(fecha[-1])
else:
    birth_date ="No existen datos"
    
if "death_date" in data['docs'][0]:
    death_date = data['docs'][0]['death_date']
else:
    death_date ="No existen datos"
     

print(f"{name} {fecha}")
print(f"{name} {death_date}")