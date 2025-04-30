from matplotlib import pyplot as plt
from tiempos import medir_tiempos_len
from tiempos import medir_tiempos_copia
from tiempos import medir_tiempos_invertir


def graficar_tiempos_len():
    #tamanos = [1, 10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    tamanos = [n for n in range(1, 1001, 20)]
    # figsize es el tamaño de la figura en pulgadas (width, height)
    plt.figure(figsize=(10, 6))

        
    tiempos = medir_tiempos_len(tamanos)

    # plot es para graficar los tiempos de ordenamiento
    # plot es el método de matplotlib para graficar
    # marker='o' es para poner un punto en cada coordenada
    plt.plot(tamanos, tiempos, marker='o', label="funcion len")

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.ylim(0, 0.0001)  # Ajusta el límite superior a 1 segundo
    plt.title('Tiempos de la funcion len')
    plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
    plt.grid() # cuadriculado
    plt.show()

def graficar_tiempos_copia():
    #tamanos = [1, 10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    tamanos = [n for n in range(1, 1001, 20)]
    # figsize es el tamaño de la figura en pulgadas (width, height)
    plt.figure(figsize=(10, 6))

        
    tiempos = medir_tiempos_copia(tamanos)

    # plot es para graficar los tiempos de ordenamiento
    # plot es el método de matplotlib para graficar
    # marker='o' es para poner un punto en cada coordenada
    plt.plot(tamanos, tiempos, marker='o', label="funcion copia")

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
   # plt.ylim(0, 0.0001)  # Ajusta el límite superior a 1 segundo
    plt.title('Tiempos de la funcion copia')
    plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
    plt.grid() # cuadriculado
    plt.show()

def graficar_tiempos_invertir():
    #tamanos = [1, 10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    tamanos = [n for n in range(1, 1001, 20)]
    # figsize es el tamaño de la figura en pulgadas (width, height)
    plt.figure(figsize=(10, 6))

        
    tiempos = medir_tiempos_invertir(tamanos)

    # plot es para graficar los tiempos de ordenamiento
    # plot es el método de matplotlib para graficar
    # marker='o' es para poner un punto en cada coordenada
    plt.plot(tamanos, tiempos, marker='o', label="funcion invertir")

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
  #  plt.ylim(0, 0.0001)  # Ajusta el límite superior a 1 segundo
    plt.title('Tiempos de la funcion invertir')
    plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
    plt.grid() # cuadriculado
    plt.show()

if __name__ == '__main__':
   graficar_tiempos_len()
   graficar_tiempos_copia()
   graficar_tiempos_invertir()
   