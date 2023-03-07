import requests
from bs4 import BeautifulSoup

list_of_titles = []
list_of_authors = []
names_authors = []
url = "https://www.buscalibre.pe/libros/ficcion/ciencia-ficcion"

response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

authors = soup.select('.autor:not(.color-dark-gray.metas.hide-on-hover)')
titles = soup.find_all('h3')

for author in authors:
    list_of_authors.append(author.get_text())
    
list_authors = list(set(list_of_authors))

    
for title in titles:
    list_of_titles.append(title.get_text())

for name in list_authors:
    part = name.split()
    if len(part) == 2:
        names_authors.append({'name': part[0], 'last_name': part[1]})
    elif len(part) == 3:
        names_authors.append({'name': part[0] + ' ' + part[1], 'last_name': part[2]})
    else:
        names_authors.append({'name': part[0], 'last_name': ''})
        
print(names_authors)