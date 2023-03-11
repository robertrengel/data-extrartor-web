import csv
from faker import Faker

fake = Faker()
data_cvs = []

for id, _ in enumerate(range(30), start=1):
    reader =  {'id':id,'firts_name': fake.first_name(), 'last_name': fake.last_name(),'nationality': fake.country(), 'age':  fake.random_int(min=10, max=100)}
    data_cvs.append(reader)
    #print(reader)
with open('readers.csv', 'w', newline='',encoding='utf-8') as archivo:
    campos = ['id','firts_name', 'last_name','nationality', 'age']
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    for dato in data_cvs:
        escritor.writerow(dato) 
print("archivo creado")  
    
# --> COPY author_author FROM 'D:\vscode project\python project\python data extrartor\authors.cvs' DELIMITER ',' CSV HEADER;
