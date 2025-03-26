def burbuja(lista):
    for pasada in range(len(lista)-1, 0, -1):
        for i in range(pasada):
            if lista[i]>lista[i+1]:
                temp=lista[i+1]
                lista[i+1]=lista[i]
                lista[i]=temp
    return lista
                
listaprueba = [5,7,5,5,4,5,5,5]
print(burbuja(listaprueba))