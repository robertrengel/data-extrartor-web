import csv

datos = [
    {'Nombre': 'Juan', 'Edad': 30, 'Ciudad': 'Buenos Aires'},
    {'Nombre': 'María', 'Edad': 25, 'Ciudad': 'Rosario'},
    {'Nombre': 'Pedro', 'Edad': 40, 'Ciudad': 'Córdoba'},
]

with open('datos.csv', 'w', newline='',encoding='utf-8') as archivo:
    campos = ['Nombre', 'Edad', 'Ciudad']
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    for dato in datos:
        escritor.writerow(dato)