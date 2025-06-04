from grafo import Grafo
from grafo import Vertice
from grafo import*
from grafo import prim
import csv

with open("docs/aldeas.txt", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    datos = []
    for fila in lector:
        if fila:  # Verifica que la fila no esté vacía
            datos.append([fila[0], fila[1].strip(), int(fila[2])])


grafo = Grafo()

for fila in datos:
    origen = fila[0]
    destino = fila[1]
    distancia = fila[2]
    grafo.agregarArista(origen, destino, distancia)  # Agrega la arista al grafo

lista_aldeas = []
for v in grafo:
    lista_aldeas.append(v.id)
lista_aldeas = sorted(lista_aldeas)
print("Aldeas:", lista_aldeas)  # Imprime la lista de aldeas

#for arista in grafo.obtenerAristas():
  #  print(f"Arista: {arista[0]} - {arista[1]}, Costo: {arista[2]}")


prim(grafo, grafo.obtenerVertice("Peligros"))  # Inicia el algoritmo Prim desde el primer vértice

print(distanciatotal(grafo))  # Imprime la distancia total del árbol de expansión mínima

predecesores_sucesores(grafo) # Imprime los predecesores y sucesores de cada vértice

adyacentes = grafo.obtenerVertice("Peligros").conectadoA
#print(f"Vértices adyacentes a 'Peligros': {[v.id for v in adyacentes]}")  # Imprime los vértices adyacentes al vértice "Peligros"

