class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None
    
    def __str__(self):
        return str( (self.dato))

class ListaDobleEnlazada:
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
    
    def __iter__(self):
        """Inicializa el iterador en la cabeza de la lista."""
        self._iterador = self.cabeza
        return self

    def __next__(self):
        """Devuelve el siguiente elemento en la iteración."""
        if self._iterador is None:
            raise StopIteration
        dato = self._iterador.dato
        self._iterador = self._iterador.siguiente
        return dato

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
    
    def insertar(self,dato,posicion=None):
        if posicion == None:
            posicion = self.tamanio
        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posicion invalida")
        
        elif posicion == 0:
            self.agregar_al_inicio(dato)

        elif posicion == self.tamanio:
            self.agregar_al_final(dato)

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
            
    def extraer(self,posicion=None):
        if posicion is None:
            posicion = self.tamanio -1
        if posicion < 0:
            posicion += self.tamanio
        if self.tamanio == 0:
            raise Exception("La lista no contiene elementos")
        elif posicion < 0 or posicion >= self.tamanio:
            raise Exception("Posicion inválida")  
        elif posicion == 0:
            item = self.cabeza.dato
            self.cabeza.siguiente.anterior = None
            self.cabeza = self.cabeza.siguiente 
            if self.cabeza is None:
                self.cola = None
            self.tamanio -= 1
            return item
        elif posicion == self.tamanio - 1:
            item = self.cola.dato
            self.cola.anterior.siguiente = None
            self.cola = self.cola.anterior
            if self.cola is None:
                self.cabeza = None
            self.tamanio -= 1
            return item
        else:
            pivote = self.cabeza
            for i in range(posicion):
                pivote = pivote.siguiente
            item = pivote.dato
            pivote.anterior.siguiente = pivote.siguiente
            pivote.siguiente.anterior = pivote.anterior
            self.tamanio -= 1
            return item
        
    def copiar(self):
        pivote = self.cabeza
        nueva_lista = ListaDobleEnlazada()
        if self.tamanio == 0:
            return nueva_lista
        else:
            for i in range (self.tamanio):
                nueva_lista.agregar_al_final(pivote.dato)
                pivote = pivote.siguiente
            return nueva_lista
        
    def invertir(self):
        pivote = self.cabeza
        nueva_lista = ListaDobleEnlazada()
        while pivote is not None:
            nueva_lista.agregar_al_inicio(pivote.dato) 
            pivote = pivote.siguiente

        self.cabeza = nueva_lista.cabeza
        self.cola = nueva_lista.cola
        self.tamanio = nueva_lista.tamanio


    def concatenar(self, lista):
        if lista.esta_vacia():
            return

        lista_copia=lista.copiar()

        if self.esta_vacia():
            self.cabeza = lista_copia.cabeza
            self.cola = lista_copia.cola
        else:
            self.cola.siguiente = lista_copia.cabeza
            lista_copia.cabeza.anterior = self.cola
            self.cola = lista_copia.cola 

        self.tamanio += lista_copia.tamanio
    
    def __add__(self, lista):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(lista)
        return nueva_lista

        
if __name__ == '__main__':
    
    lista = ListaDobleEnlazada()
    lista.agregar_al_final(1)
    lista.agregar_al_final(2)
    lista.agregar_al_final(3)
    lista.agregar_al_inicio(0)
    lista.agregar_al_final(6)
    lista.agregar_al_final(8)
    lista.agregar_al_inicio(12)
    lista.insertar(9,2)
    listacop = lista.copiar()
    lista.invertir()
    
    lista2 = lista+listacop

    pivote = lista2.cabeza
    for i in range(lista2.tamanio):
        print(pivote)
        pivote = pivote.siguiente
    print("Tamanio")
    pivote = lista.cabeza
    for i in range(lista.tamanio):
        print(pivote)
        pivote = pivote.siguiente
    

