from grafo import Grafo
from grafo import Vertice
from grafo import prim
import csv

with open("docs/aldeas.txt", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    datos = []
    for fila in lector:
        if fila:  # Verifica que la fila no esté vacía
            datos.append(fila)

