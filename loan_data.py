import csv
from datetime import datetime
from faker import Faker

faker = Faker()
category_data = []
start_date_loan = datetime(2020, 1, 1)
end_date_loan = datetime(2021, 12, 31)
start_date_return = datetime(2022, 1, 1)
end_date_return = datetime(2022, 12, 31)

        
for id in range(1,31):
    relation_dict = {'id': id,
                     'loan_date': faker.date_between(start_date=start_date_loan, end_date=end_date_loan),
                     'return_date': faker.date_between(start_date=start_date_return, end_date=end_date_return),
                     'retuned': False,
                     'book_id': faker.random_int(min=1, max=50),
                     'reader_id': faker.random_int(min=1, max=30),}
    category_data.append(relation_dict) 

with open('loan_data.csv', 'w', newline='',encoding='utf-8') as archivo:
    campos = ['id','loan_date','return_date','retuned','book_id','reader_id']
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    for dato in category_data:
        escritor.writerow(dato) 
print("archivo creado") 