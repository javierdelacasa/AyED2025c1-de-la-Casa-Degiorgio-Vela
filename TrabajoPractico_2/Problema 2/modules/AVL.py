class Nodo:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.cargautil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    def esHijoIzquierdo(self):
        return self.padre is not None and self.padre.hijoIzquierdo == self
    
    def esHijoDerecho(self):
        return self.padre is not None and self.padre.hijoDerecho == self

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo is not None
    
    def tieneHijoDerecho(self):   
        return self.hijoDerecho is not None
    
    def esRaiz(self):
        return self.padre is None
    
    def _obtenermaximo(self):
        cargautil_max = self.cargautil
        clave_max = self.clave
        if self.tieneHijoIzquierdo():
            hijo_clave_max, hijo_cargautil_max = self.hijoIzquierdo._obtenermaximo()
            if hijo_cargautil_max > cargautil_max:
                cargautil_max = hijo_cargautil_max
                clave_max = hijo_clave_max
        if self.tieneHijoDerecho():
            hijo_clave_max, hijo_cargautil_max = self.hijoDerecho._obtenermaximo()
            if hijo_cargautil_max > cargautil_max:
                cargautil_max = hijo_cargautil_max
                clave_max = hijo_clave_max
        return clave_max, cargautil_max

    def _obtenerminimo(self):
        cargautil_min = self.cargautil
        clave_min = self.clave
        if self.tieneHijoIzquierdo():
            hijo_clave_min, hijo_cargautil_min = self.hijoIzquierdo._obtenerminimo()
            if hijo_cargautil_min < cargautil_min:
                cargautil_min = hijo_cargautil_min
                clave_min = hijo_clave_min
        if self.tieneHijoDerecho():
            hijo_clave_min, hijo_cargautil_min = self.hijoDerecho._obtenerminimo()
            if hijo_cargautil_min < cargautil_min:
                cargautil_min = hijo_cargautil_min
                clave_min = hijo_clave_min
        return clave_min, cargautil_min
    
    def _obtenerminimo_rango(self, inicio, fin):
        clave_min, cargautil_min = None, float('inf')

        # Verificar si el nodo actual está dentro del rango
        if inicio <= self.clave <= fin:
            clave_min, cargautil_min = self.clave, self.cargautil

        # Recorrer el hijo izquierdo si existe
        if self.tieneHijoIzquierdo():
            hijo_clave_min, hijo_cargautil_min = self.hijoIzquierdo._obtenerminimo_rango(inicio, fin)
            if hijo_cargautil_min < cargautil_min:
                clave_min, cargautil_min = hijo_clave_min, hijo_cargautil_min

        # Recorrer el hijo derecho si existe
        if self.tieneHijoDerecho():
            hijo_clave_min, hijo_cargautil_min = self.hijoDerecho._obtenerminimo_rango(inicio, fin)
            if hijo_cargautil_min < cargautil_min:
                clave_min, cargautil_min = hijo_clave_min, hijo_cargautil_min

        return clave_min, cargautil_min

    def _obtenermaximo_rango(self, inicio, fin):
        clave_max, cargautil_max = None, float('-inf')

        # Verificar si el nodo actual está dentro del rango
        if inicio <= self.clave <= fin:
            clave_max, cargautil_max = self.clave, self.cargautil

        # Recorrer el hijo izquierdo si existe
        if self.tieneHijoIzquierdo():
            hijo_clave_max, hijo_cargautil_max = self.hijoIzquierdo._obtenermaximo_rango(inicio, fin)
            if hijo_cargautil_max > cargautil_max:
                clave_max, cargautil_max = hijo_clave_max, hijo_cargautil_max

        # Recorrer el hijo derecho si existe
        if self.tieneHijoDerecho():
            hijo_clave_max, hijo_cargautil_max = self.hijoDerecho._obtenermaximo_rango(inicio, fin)
            if hijo_cargautil_max > cargautil_max:
                clave_max, cargautil_max = hijo_clave_max, hijo_cargautil_max

        return clave_max, cargautil_max
    
    def preorden(self):
        print(self.clave)
        if self.hijoIzquierdo:
            self.hijoIzquierdo.preorden()
        if self.hijoDerecho:
            self.hijoDerecho.preorden()
    
    def preorden_rango(self, inicio, fin):
        if inicio <= self.clave <= fin:
            print(self.clave)
        if self.tieneHijoIzquierdo() and self.clave > inicio:
            self.hijoIzquierdo.preorden_rango(inicio, fin)
        if self.tieneHijoDerecho() and self.clave < fin:
            self.hijoDerecho.preorden_rango(inicio, fin)

    def preorden_obtencion(self):
        print(self.cargautil)
        if self.hijoIzquierdo:
            self.hijoIzquierdo.preorden_obtencion()
        if self.hijoDerecho:
            self.hijoDerecho.preorden_obtencion()
    
    def preorden_rango_obtencion(self, inicio, fin):
        if inicio <= self.clave <= fin:
            print(self.cargautil)
        if self.tieneHijoIzquierdo() and self.clave > inicio:
            self.hijoIzquierdo.preorden_rango_obtencion(inicio, fin)
        if self.tieneHijoDerecho() and self.clave < fin:
            self.hijoDerecho.preorden_rango_obtencion(inicio, fin)

class Arbol:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def tamanio(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def __iter__(self):
        return self.raiz.__iter__()
    
    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = Nodo(clave,valor)
        self.tamano = self.tamano + 1

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
                if nodoActual.tieneHijoIzquierdo():
                        self._agregar(clave,valor,nodoActual.hijoIzquierdo)
                else:
                        nodoActual.hijoIzquierdo = Nodo(clave,valor,padre=nodoActual)
                        self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                    self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                    nodoActual.hijoDerecho = Nodo(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoDerecho)

    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                    nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)

    def rotarIzquierda(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)

    def rotarDerecha(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 - max(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + min(rotRaiz.factorEquilibrio, 0)

    def reequilibrar(self,nodo):
        if nodo.factorEquilibrio < 0:
                if nodo.hijoDerecho.factorEquilibrio > 0:
                    self.rotarDerecha(nodo.hijoDerecho)
                    self.rotarIzquierda(nodo)
                else:
                    self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
                if nodo.hijoIzquierdo.factorEquilibrio < 0:
                    self.rotarIzquierda(nodo.hijoIzquierdo)
                    self.rotarDerecha(nodo)
                else:
                    self.rotarDerecha(nodo)

    def obtener(self, clave):
        actual = self.raiz
        while True:
            if actual.clave == clave:
                return actual.cargautil
            elif actual.clave < clave and actual.tieneHijoDerecho():
                    actual = actual.hijoDerecho
            elif actual.clave > clave and actual.tieneHijoIzquierdo():
                    actual = actual.hijoIzquierdo
            else:
                return None
            
    def __getitem__(self,clave):
        return self.obtener(clave)

    def obtenermaximo(self):
        if self.raiz is not None:
            return self.raiz._obtenermaximo()
        return None

    def obtenerminimo(self):
        if self.raiz is not None:
            return self.raiz._obtenerminimo()
        return None
    
    def obtenermaximo_rango(self,inicio, fin):
        if self.raiz is not None:
            return self.raiz._obtenermaximo_rango(inicio, fin)
        return None

    def obtenerminimo_rango(self,inicio, fin):
        if self.raiz is not None:
            return self.raiz._obtenerminimo_rango(inicio, fin)
        return None

    def preorden_visualizacion(self):
        if self.raiz is not None:
            self.raiz.preorden()
        else:
            print("El árbol está vacío.")

    def preorden_rango_visualizacion(self, inicio, fin):
        if self.raiz is not None:
            self.raiz.preorden_rango(inicio, fin)
        else:
            print("El árbol está vacío.")

    def preorden_obtencion(self):
        if self.raiz is not None:
            self.raiz.preorden_obtencion()
        else:
            print("El árbol está vacío.")

    def preorden_rango_obtencion(self, inicio, fin):
        if self.raiz is not None:
            self.raiz.preorden_rango_obtencion(inicio, fin)
        else:
            print("El árbol está vacío.")

if __name__ == "__main__":
    arbol = Arbol()
    for clave in [46,34.5,25,12.23,30, 20, 10, 3 ,2, 1]:
        arbol.agregar(clave, clave * 2)
    print("Tamaño del árbol:", arbol.tamanio())
    print("Raíz del árbol:", arbol.raiz.clave)
    #Deberia de imprimir el tamaño del árbol, la raíz, sus hijos y los factores de equilibrio. Esto es: 
    print(arbol.raiz.hijoIzquierdo.clave)
    print(arbol.raiz.hijoDerecho.clave)
    print(arbol.raiz.hijoIzquierdo.factorEquilibrio)
    print(arbol.obtener(30))
    print(arbol.obtener(2))
    print(arbol.obtenermaximo())
    print(arbol.obtenerminimo())
    print(arbol.obtenermaximo_rango(0, 40))
    print(arbol.obtenerminimo_rango(9, 20))
    


    #Prueba rotaciones
    arbol1 = Arbol()
    for clave in [1,2,4,3,5,6,7]:
        arbol1.agregar(clave, clave * 2)
    arbol1.preorden_visualizacion()
