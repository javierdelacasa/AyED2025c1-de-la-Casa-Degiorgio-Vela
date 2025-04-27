from random import randint
import time
from ListaDobleEnlazada import ListaDobleEnlazada

def medir_tiempos_len(tamanos):
    
    tiempos_len= []

    for n in tamanos:
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(randint(1, 1000))
            
        inicio = time.perf_counter()
        lista.__len__
        fin = time.perf_counter()
        tiempos_len.append(fin - inicio)
        print(f"Tiempo de funcion len para n={n}: {fin - inicio:.10f} segundos")
    
    return tiempos_len  

def medir_tiempos_copia(tamanos):
    
    tiempos_copia = []
    
    for n in tamanos:
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(randint(1, 1000))
        inicio = time.perf_counter()
        lista.copiar
        fin = time.perf_counter()
        tiempos_copia.append(fin - inicio)
        print(f"Tiempo de funcion copia para n={n}: {fin - inicio:.10f} segundos")
    
    return tiempos_copia

def medir_tiempos_invertir(tamanos):
    
    tiempos_invertir = []
    
    for n in tamanos:
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(randint(1, 1000))
        inicio = time.perf_counter()
        lista.invertir
        fin = time.perf_counter()
        tiempos_invertir.append(fin - inicio)
        print(f"Tiempo de funcion invertir para n={n}: {fin - inicio:.10f} segundos")
    
    return tiempos_invertir
        
        

    

if __name__ == '__main__':
    tamanos = [1, 10, 100, 200, 500, 700, 1000, 1000000]
    
    medir_tiempos_len(tamanos)
    
    medir_tiempos_copia(tamanos)
    
    medir_tiempos_invertir(tamanos)