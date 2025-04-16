class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None
    
    def __str__(self):
        return str( (self.dato))

class listaDE:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def esta_vacia(self):
        if self.cabeza == None:
            return True
        else:
            return False
        
    def __len__(self):
        return self.tamanio
    
    def agregar_al_inicio(self,dato):
        nuevo_nodo = nodo(dato)
        if self.tamanio == 0:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cabeza.anterior = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.tamanio +=1
    
    def agregar_al_final(self,dato):
        nuevo_nodo = nodo(dato)
        if self.tamanio == 0:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.tamanio +=1
    
    def insertar(self,dato,posicion):
        if posicion == None:
            posicion = self.tamanio
        if posicion < 0 or posicion > self.tamanio:
            raise Exception ("Posicion invalida")
        
        elif posicion == 0:
            self.agregar_al_inicio(dato)
            self.tamanio +=1

        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
            self.tamanio +=1

        else:
            nuevo_nodo= nodo(dato)
            pivote=self.cabeza

            for i in range(posicion):
                pivote = pivote.siguiente

            nuevo_nodo.anterior = pivote.anterior
            nuevo_nodo.siguiente = pivote
            pivote.anterior.siguiente = nuevo_nodo
            pivote.anterior = nuevo_nodo
            self.tamanio +=1
            
    def extraer(self,dato,posicion):
        if posicion == None:
            posicion = self.tamanio
        if self.tamanio == 0:
            raise Exception ("La lista no contiene elementos")
        elif posicion < 0 or posicion > self.tamanio:
            raise Exception ("Posicion invalida")  
        elif posicion == 0:
            item= self.cabeza
            self.cabeza.siguiente.anterior = None
            self.cabeza = self.cabeza.siguiente 
            self.tamanio -=1
            return item
        elif posicion == self.tamanio:
            item = self.cola
            self.cola.anterior.siguiente = None
            self.cola= self.cola.anterior
            self.tamanio -= 1
            return item
        else:
            pivote=self.cabeza

            for i in range(posicion):
                pivote = pivote.siguiente

            item = pivote
            pivote.anterior.siguiente = pivote.siguiente
            pivote.siguiente.anterior = pivote.anterior
            self.tamanio -=1
            return item
    def copiar(self):
        pivote = self.cabeza
        nueva_lista = listaDE()
        if self.tamanio == 0:
            return listaDE
        else:
            for i in range (self.tamanio):
                listaDE.agregar_al_final = pivote
                pivote = pivote.siguiente
            return listaDE
        
    def invertir(self):
        pivote = self.cabeza
        nueva_lista = listaDE()
        if self.tamanio == 0:
            self = listaDE
        else:
            for i in range (self.tamanio):
                nueva_lista.agregar_al_inicio = pivote
                pivote = pivote.siguiente
            self = nueva_lista

if __name__ == '__main__':
    print(  nodo(4))

    lista = listaDE()
    lista.agregar_al_final(1)
    lista.agregar_al_final(2)
    lista.agregar_al_final(3)
    lista.agregar_al_inicio(0)
    lista.insertar(9,2)
    listacop = lista.copiar
    lista.invertir()
    

    pivote = lista.cabeza
    for i in range(lista.tamanio):
        print(pivote)
        pivote = pivote.siguiente

