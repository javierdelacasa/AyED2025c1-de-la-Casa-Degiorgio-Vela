#A partir de un valor pivote, ordena parcialmente, donde los valores menores al pivote quedan a la izquierda y los mayores a la derecha. 
# Modifica la lista y devuelve el punto de division (ubicacion del pivote)
def particion(unaLista,primero,ultimo):
   #Tomamos el primer elemento de la lista como el valor pivote
    valorPivote = unaLista[primero]

    #Marcaizq inicia como el indice del elemento siguiente al valor pivote 
    # Es una variable creciente, varia como indice de la lista y compara el valor correspondiente de la lista con el pivote
    marcaIzq = primero+1

   #Marcader inicia como el indice del ultimo elemento de la lista
# Es una variable decreciente, varia como indice de la lista y compara el valor correspondiente de la lista con el pivote
    marcaDer = ultimo

    vuelta_completa = False
    while not vuelta_completa:


#La marcaizq se va a mover hasta que su valor correspondiente en la lista sea mayor al valor pivote o que sea igual o mayor a la marca derecha
        while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
            marcaIzq = marcaIzq + 1

#La marcader se va a mover hasta que su valor correspondiente en la lista sea menor al valor pivote o que sea igual o menor a la marca izquierda
        while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
            marcaDer = marcaDer -1

#Cuando las marcas se cruzas es porque ya estan parcialmente ordenados los elementos, con los menores a la izquierda del pivote y los mayores a la derecha
        if marcaDer < marcaIzq:
            vuelta_completa = True

#Si las marcas no se cruzaron, intercambiamos los valores asociados. Y se repite el ciclo while inicial. 
        else:
            temp = unaLista[marcaIzq]
            unaLista[marcaIzq] = unaLista[marcaDer]
            unaLista[marcaDer] = temp

# intercambia los valores del elemento  correspondiente a la marca derecha y el del pivote
    temp = unaLista[primero]
    unaLista[primero] = unaLista[marcaDer]
    unaLista[marcaDer] = temp


    return marcaDer


def ordenamientoRapidoAuxiliar(unaLista,primero,ultimo):
    if primero<ultimo:

        #la funcion partición ordena parcialmente la lista y retorna el punto de division
        puntoDivision = particion(unaLista,primero,ultimo)

        #llamamos recursivamente a la funcion dos veces con la parte previa y siguiente al punto de division como indices
        ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)
        ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo)


def ordenamientoRapido(unaLista):
    #primer llamado a la funcion auxiliar
    ordenamientoRapidoAuxiliar(unaLista,0,len(unaLista)-1)


if __name__ == "__main__":
    from random import randint
    listaprueba = [randint(10000,99999) for _ in range(15)]
    ordenamientoRapido(listaprueba)
    print(listaprueba)