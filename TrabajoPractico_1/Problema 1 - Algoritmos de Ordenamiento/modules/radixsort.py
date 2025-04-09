#El metodo de counting es muy eficiente para numeros positivos menores a 10, esto por como funciona al generar una lista a partir de arreglo inicial.
#Primero aplicaremos counting y se repetira variando entre unidades, decenas, centenas, etc. En eso se basa el Radix Sort, donde se realizan varios counting para poder aplicarlo en numeros de valores mayores a 10.
def counting_sort(lista):
    max_val = max(lista)
    
    cantidad = [0] * (max_val + 1)
    
    
    for nro in lista:
        cantidad[nro] += 1
    
    lista_ordenada = []
    for i, valor in enumerate(count):
        lista_ordenada.extend([i] * valor)
    
    return lista_ordenada
