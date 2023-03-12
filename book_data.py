import csv
import requests
from bs4 import BeautifulSoup
from faker import Faker



#url_api = "https://openlibrary.org/search/authors.json?q="
#url_api_author = "https://openlibrary.org/authors/"
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



