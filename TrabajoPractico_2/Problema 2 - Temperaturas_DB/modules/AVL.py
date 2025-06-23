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
    
    def tieneAlgunHijo(self):
        return self.tieneHijoIzquierdo() or self.tieneHijoDerecho()
    
    def esRaiz(self):
        return self.padre is None
    
    def _obtenermaximo(self): #funcion auxiliar de obtenermaximo
        cargautil_max = self.cargautil
        clave_max = self.clave
        #Actua de manera recursiva
        if self.tieneHijoIzquierdo():
            hijo_clave_max, hijo_cargautil_max = self.hijoIzquierdo._obtenermaximo()
            if hijo_cargautil_max > cargautil_max: #se guarda la carga util mayor
                cargautil_max = hijo_cargautil_max
                clave_max = hijo_clave_max
        if self.tieneHijoDerecho():
            hijo_clave_max, hijo_cargautil_max = self.hijoDerecho._obtenermaximo()
            if hijo_cargautil_max > cargautil_max:
                cargautil_max = hijo_cargautil_max
                clave_max = hijo_clave_max
        return clave_max, cargautil_max #clave asociada a la carga util maxima y carga util maxima

    def _obtenerminimo(self): #funcion auxiliar de obtenerminimo
        cargautil_min = self.cargautil
        clave_min = self.clave
        #Actua de manera recursiva
        if self.tieneHijoIzquierdo():
            hijo_clave_min, hijo_cargautil_min = self.hijoIzquierdo._obtenerminimo()
            if hijo_cargautil_min < cargautil_min:# se guarda la carga util menor
                cargautil_min = hijo_cargautil_min
                clave_min = hijo_clave_min
        if self.tieneHijoDerecho():
            hijo_clave_min, hijo_cargautil_min = self.hijoDerecho._obtenerminimo()
            if hijo_cargautil_min < cargautil_min:
                cargautil_min = hijo_cargautil_min
                clave_min = hijo_clave_min
        return clave_min, cargautil_min #clave asociada a la carga util minima y carga util minima
    
    def _obtenerminimo_rango(self, inicio, fin):
        clave_min, cargautil_min = None, float('inf')
        # Verificar si el nodo actual está dentro del rango 
        if inicio <= self.clave <= fin:
            clave_min, cargautil_min = self.clave, self.cargautil
        # Actua recursivamente
        if self.tieneHijoIzquierdo():
            hijo_clave_min, hijo_cargautil_min = self.hijoIzquierdo._obtenerminimo_rango(inicio, fin)
            if hijo_cargautil_min < cargautil_min:
                clave_min, cargautil_min = hijo_clave_min, hijo_cargautil_min
        if self.tieneHijoDerecho():
            hijo_clave_min, hijo_cargautil_min = self.hijoDerecho._obtenerminimo_rango(inicio, fin)
            if hijo_cargautil_min < cargautil_min:
                clave_min, cargautil_min = hijo_clave_min, hijo_cargautil_min

        return clave_min, cargautil_min

    def _obtenermaximo_rango(self, inicio, fin):
        clave_max, cargautil_max = None, float('-inf')
        # Verifica si el nodo actual está dentro del rango
        if inicio <= self.clave <= fin:
            clave_max, cargautil_max = self.clave, self.cargautil
        # Actua recursivamente
        if self.tieneHijoIzquierdo():
            hijo_clave_max, hijo_cargautil_max = self.hijoIzquierdo._obtenermaximo_rango(inicio, fin)
            if hijo_cargautil_max > cargautil_max:
                clave_max, cargautil_max = hijo_clave_max, hijo_cargautil_max
        if self.tieneHijoDerecho():
            hijo_clave_max, hijo_cargautil_max = self.hijoDerecho._obtenermaximo_rango(inicio, fin)
            if hijo_cargautil_max > cargautil_max:
                clave_max, cargautil_max = hijo_clave_max, hijo_cargautil_max

        return clave_max, cargautil_max
    
    def preorden(self): #funcion auxiliar de preorden_visualizacion
        print(self.clave) # imprime la clave del nodo
        if self.hijoIzquierdo:
            self.hijoIzquierdo.preorden()
        if self.hijoDerecho:
            self.hijoDerecho.preorden()
    
    def preorden_rango(self, inicio, fin): #funcion auxiliar de preorden_rango_visualizacion
        # Verifica si la clave del nodo actual está dentro del rango
        if inicio <= self.clave <= fin:
            print(self.clave)
        if self.tieneHijoIzquierdo() and self.clave > inicio:
            self.hijoIzquierdo.preorden_rango(inicio, fin)
        if self.tieneHijoDerecho() and self.clave < fin:
            self.hijoDerecho.preorden_rango(inicio, fin)
 
    def preorden_obtencion(self):# funcion auxiliar de preorden_obtencion
        print(self.cargautil) # imprime la carga util del nodo
        if self.hijoIzquierdo:
            self.hijoIzquierdo.preorden_obtencion()
        if self.hijoDerecho:
            self.hijoDerecho.preorden_obtencion()
    
    def preorden_rango_obtencion(self, inicio, fin): # funcion auxiliar de preorden_rango_obtencion
        # Verifica si está dentro del rango
        if inicio <= self.clave <= fin:
            print(self.clave,self.cargautil) # imprime la clave y la carga util del nodo
        if self.tieneHijoIzquierdo() and self.clave > inicio:
            self.hijoIzquierdo.preorden_rango_obtencion(inicio, fin)
        if self.tieneHijoDerecho() and self.clave < fin:
            self.hijoDerecho.preorden_rango_obtencion(inicio, fin)

    def esHoja(self):
        return not self.tieneHijoIzquierdo() and not self.tieneHijoDerecho()
    
    def tieneAmbosHijos(self):
        return self.tieneHijoIzquierdo() and self.tieneHijoDerecho()
    
    def reemplazarDatoDeNodo(self, clave, valor, hijoIzquierdo, hijoDerecho):
        self.clave = clave
        self.cargautil = valor
        self.hijoIzquierdo = hijoIzquierdo
        self.hijoDerecho = hijoDerecho
        if hijoIzquierdo:
            hijoIzquierdo.padre = self
        if hijoDerecho:
            hijoDerecho.padre = self

    def encontrarSucesor(self):
        suc = None
        if self.tieneHijoDerecho(): # si tiene hijo derecho, el sucesor es el mínimo del subárbol derecho
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre: 
                if self.esHijoIzquierdo(): # si es hijo izquierdo, el sucesor es el padre
                    suc = self.padre
                else: # si es hijo derecho, se busca el sucesor en el padre
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo(): #el minimo se encuentra en el extremo izquierdo
            actual = actual.hijoIzquierdo
        return actual

    def empalmar(self):
        if self.esHoja(): # si es hoja, simplemente se elimina
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo(): # se conectan las referencias entre el padre y algun hijo
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre

    def __iter__(self): # permite iterar sobre el nodo y sus hijos con un inorden
        if self.hijoIzquierdo:
            yield from self.hijoIzquierdo # se ejecuta sobre el hijo izquierdo
        yield self.clave, self.cargautil # devuelve la clave y la carga util del nodo
        if self.hijoDerecho:
            yield from self.hijoDerecho # se ejecuta sobre el hijo derecho

class Arbol:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def tamanio(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def __iter__(self):
        return self.raiz.__iter__() ######
    
    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = Nodo(clave,valor) #si el arbol está vacío, se crea un nuevo nodo raíz
        self.tamano = self.tamano + 1

    def _agregar(self,clave,valor,nodoActual): #funcion auxiliar de agregar
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                    self._agregar(clave,valor,nodoActual.hijoIzquierdo) #se ejecuta recursivamente
            else:
                    nodoActual.hijoIzquierdo = Nodo(clave,valor,padre=nodoActual) #se crea el nodo en su lugar
                    self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                    self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                    nodoActual.hijoDerecho = Nodo(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoDerecho)

    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1: # si esta desequilibrado se reequilibra
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:  # si no es raiz se actualiza el fe del padre
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

    def reequilibrar(self,nodo): # realiza las rotaciones que correspondan
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
            if actual.clave == clave: # comprueba en cada nodo si la clave es la buscada
                return actual.cargautil
            # cambia el actual y repite el ciclo
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
            return self.raiz._obtenermaximo() #llama a la funcion auxiliar sobre la raiz
        return None

    def obtenerminimo(self):
        if self.raiz is not None:
            return self.raiz._obtenerminimo() #llama a la funcion auxiliar sobre la raiz
        return None
    
    def obtenermaximo_rango(self,inicio, fin):
        if self.raiz is not None:
            return self.raiz._obtenermaximo_rango(inicio, fin) #llama a la funcion auxiliar sobre la raiz
        return None

    def obtenerminimo_rango(self,inicio, fin):
        if self.raiz is not None:
            return self.raiz._obtenerminimo_rango(inicio, fin) #llama a la funcion auxiliar sobre la raiz
        return None

    def preorden_visualizacion(self):
        if self.raiz is not None:
            self.raiz.preorden() #llama a la funcion auxiliar sobre la raiz
        else:
            print("El árbol está vacío.")

    def preorden_rango_visualizacion(self, inicio, fin):
        if self.raiz is not None:
            self.raiz.preorden_rango(inicio, fin) #llama a la funcion auxiliar sobre la raiz
        else:
            print("El árbol está vacío.")

    def preorden_obtencion(self):
        if self.raiz is not None:
            self.raiz.preorden_obtencion() #llama a la funcion auxiliar sobre la raiz
        else:
            print("El árbol está vacío.")

    def preorden_rango_obtencion(self, inicio, fin):
        if self.raiz is not None:
            self.raiz.preorden_rango_obtencion(inicio, fin) #llama a la funcion auxiliar sobre la raiz
        else:
            print("El árbol está vacío.")

    def remover (self,nodoActual):
        if nodoActual.esHoja(): #si es hoja, simplemente se elimina
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos(): #interior
            # se busca el sucesor, se empalma y se reemplaza la clave y la carga util
            suc = nodoActual.encontrarSucesor()
            suc.empalmar()
            nodoActual.clave = suc.clave
            nodoActual.cargautil = suc.cargautil
        else: # (1) hijo
            if nodoActual.tieneHijoIzquierdo():
                # se conecta el padre con el hijo izquierdo
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else: # si es la raiz, se reemplaza el nodo actual por el hijo izquierdo
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
                                        nodoActual.hijoIzquierdo.cargautil,
                                        nodoActual.hijoIzquierdo.hijoIzquierdo,
                                        nodoActual.hijoIzquierdo.hijoDerecho)
                    nodoActual.padre = None 
            else: # si tiene hijo derecho, se conecta el padre con el hijo derecho
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else: # si es la raiz, se reemplaza el nodo actual por el hijo derecho
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
                                        nodoActual.hijoDerecho.cargautil,
                                        nodoActual.hijoDerecho.hijoIzquierdo,
                                nodoActual.hijoDerecho.hijoDerecho)    
                    
    def eliminar(self,clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave, self.raiz) # busca el nodo a eliminar
            if nodoAEliminar:
                self.remover(nodoAEliminar) # llama a la funcion auxiliar de remover
                self.tamano = self.tamano-1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave: # si es el único nodo, se elimina la raíz
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')
        self.reequilibrar(nodoAEliminar)

    def __delitem__(self,clave):
        self.eliminar(clave)

    def _obtener(self, clave, nodoActual):
        # función auxiliar de obtener, busca el nodo con la clave dada, recursivamente
        if nodoActual is None:
            return None
        if nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave and nodoActual.tieneHijoIzquierdo():
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        elif clave > nodoActual.clave and nodoActual.tieneHijoDerecho():
            return self._obtener(clave, nodoActual.hijoDerecho)
        else:
            return None
        
    def __iter__(self):
        if self.raiz is not None:
            yield from self.raiz #delega la iteración al nodo raíz
        


if __name__ == "__main__":
    arbol = Arbol()
    for clave in [46,34.5,25,12.23,30, 20, 10, 3 ,2, 1]:
        arbol.agregar(clave, clave * 2)