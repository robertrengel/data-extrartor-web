import csv
from faker import Faker

faker = Faker()

words = []
category_data = []

while True:
    word = faker.word()
    if len(word) >= 7 and word not in words:
        words.append(word)
    if len(words) >= 17:
        break
        
for id, i in enumerate(words, start=1):
    category_dict = {'id': id, 'name': i}
    category_data.append(category_dict)
    

with open('cateegories_data.csv', 'w', newline='',encoding='utf-8') as archivo:
    campos = ['id','name']
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    for dato in category_data:
        escritor.writerow(dato) 
print("archivo creado") 