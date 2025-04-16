#El metodo de counting es muy eficiente para numeros positivos menores a 10, esto por como funciona al generar una lista a partir de arreglo inicial.
#Primero aplicaremos counting y se repetira variando entre unidades, decenas, centenas, etc. En eso se basa el Radix Sort, donde se realizan varios counting para poder aplicarlo en numeros de valores mayores a 10.
def counting_sort(arr, exp):

    n = len(arr)  # Obtener la longitud de la lista
    output = [0] * n  # Crear una lista de salida del mismo tamaño que la lista original
    count = [0] * 10  # Crear una lista de conteo para los dígitos (0-9)

    # Contar la frecuencia de cada dígito en la lista
    for i in range(n):
        index = arr[i] // exp  # Calcular el índice del dígito actual
        count[index % 10] += 1  # Incrementar el conteo del dígito en la lista de conteo

    # Calcular las posiciones finales de los elementos en la lista de salida
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir la lista de salida en orden ascendente según el dígito actual
    i = n - 1

    while i >= 0:
        index = arr[i] // exp  # Calcular el índice del dígito actual
        output[count[index % 10] - 1] = arr[i]  # Colocar el elemento en la posición correcta en la lista de salida
        count[index % 10] -= 1  # Reducir el conteo del dígito
        i -= 1

    # Copiar los elementos ordenados de la lista de salida a la lista original
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(lista):
    max_num = max(lista)  # Obtener el número máximo en la lista
    exp = 1
    while max_num // exp > 0:

        counting_sort(lista, exp)  # Llamar al counting_sort para ordenar los elementos en base al dígito actual
        exp *= 10  # Mover al siguiente dígito hacia la izquierda


if __name__ == '__main__':
    lista = [992, 5, 115, 12, 89, 99]
    print("Lista desordenada:", lista)
    radix_sort(lista)
    print("Lista ordenada:", lista)