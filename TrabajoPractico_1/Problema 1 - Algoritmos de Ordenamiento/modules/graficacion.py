from matplotlib import pyplot as plt
from tiempos import medir_tiempos

def graficar_tiempos(lista_metodos_ord):
    #tamanos = [1, 10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    tamanos = [n for n in range(1, 1001, 20)]
    # figsize es el tamaño de la figura en pulgadas (width, height)
    plt.figure(figsize=(10, 6))

    for metodo_ord in lista_metodos_ord:
        
        tiempos = medir_tiempos(metodo_ord, tamanos)

        # plot es para graficar los tiempos de ordenamiento
        # plot es el método de matplotlib para graficar
        # marker='o' es para poner un punto en cada coordenada
        plt.plot(tamanos, tiempos, marker='o', label=metodo_ord.__name__)

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
    plt.grid() # cuadriculado
    plt.show()

if __name__ == '__main__':
   from burbuja import burbuja
   from quicksort import ordenamientoRapido
   from radixsort import radix_sort
   graficar_tiempos([burbuja, ordenamientoRapido,radix_sort])
   