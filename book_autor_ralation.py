import csv
from faker import Faker

faker = Faker()

category_data = []


        
for id in range(1,51):
    relation_dict = {'id': id, 'book_id': id, 'autor_id': faker.random_int(min=1, max=17)}
    category_data.append(relation_dict)
    

with open('relation_data.csv', 'w', newline='',encoding='utf-8') as archivo:
    campos = ['id','book_id','autor_id']
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    for dato in category_data:
        escritor.writerow(dato) 
print("archivo creado") 