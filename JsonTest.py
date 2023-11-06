import json

with open('test.json', 'r') as archivo:
    # Carga el contenido JSON en una variable
    datos = json.load(archivo)

print(datos['intereses'][2])