import requests
from bs4 import BeautifulSoup

soup_local = ""
url = "https://www.buscalibre.pe/libros/ficcion/ciencia-ficcion"
response = requests.get(url)
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')

with open('parse.txt', 'w', encoding='utf-8') as f:
     f.write(response.text)
     

