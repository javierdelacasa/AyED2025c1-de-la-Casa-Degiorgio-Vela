def burbuja(lista):
    for pasada in range(len(lista)-1, 0, -1):
        for i in range(pasada):
            if lista[i]>lista[i+1]:
                temp=lista[i+1]
                lista[i+1]=lista[i]
                lista[i]=temp
    return lista


if __name__ =="__main__":
    listaprueba = [5,7,5,5,4,5,1,3,76,4,2,-1,3,123,12356,1223,1,5,5]
    print(burbuja(listaprueba))