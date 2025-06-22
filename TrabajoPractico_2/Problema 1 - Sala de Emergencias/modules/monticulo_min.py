class monticulo():
    def __init__(self):
        self.lista = [None] # Crea la lista vacía a usarse como montículo
        self.tam = 0 # Inicia el contador de elementos en el montículo
    
    def insertar(self,dato,param1=None, param2=None): # Inserta un elemento en el montículo. De base, sin parámetros
        self.lista.append(dato) # Añade el dato al final de la lista
        self.tam = self.tam + 1 # Aumenta el contador de elementos
        self.infiltArriba(self.tam, param1, param2) # Infiltra el elemento desde el final de la lista hasta su posición

    def infiltArriba(self, i, param1=None, param2=None): # Infiltra el elemento hacia arriba en el montículo
        if param1 is None or param2 is None: # Si no se especifican parámetros, se usa el comportamiento original (basandose en el valor 'i')
            while i // 2 > 0: # Comprueba si el elemento tiene un padre (no es raíz)
                if self.lista[i] < self.lista[i // 2]: # Comprueba si el elemento es menor al padre
                    self.lista[i], self.lista[i // 2] = self.lista[i // 2], self.lista[i] # Intercambia el elemento con su padre
                i = i // 2 # Actualiza el índice del elemento a su nueva posición
        else: #Si se especifican parámetros, se usa el comportamiento modificado (basandose en los parametros especificados)
            while i // 2 > 0: 
                if self._comparar(self.lista[i], self.lista[i // 2], param1, param2): # Llama a la función de comparación
                    self.lista[i], self.lista[i // 2] = self.lista[i // 2], self.lista[i] # Intercambia el elemento con su padre
                i = i // 2 # Actualiza el índice del elemento a su nueva posición

    def _comparar(self, a, b, param1, param2): # Compara los elementos 'a' y 'b', con respecto a los parametros especificados
        v1a = self._obtener_valor(a, param1) 
        v1b = self._obtener_valor(b, param1)
        if v1a < v1b: # Compara con respecto al parámetro 'param1' (primario)
            return True
        elif v1a == v1b: # Si son iguales, se compara con el segundo parámetro
            v2a = self._obtener_valor(a, param2)
            v2b = self._obtener_valor(b, param2)
            return v2a < v2b # Compara con respecto al parámetro 'param2' (secundario)
        else:
            return False

    def _obtener_valor(self, elem, param): # Obtiene el valor de un elemento 'elem' con respecto al parámetro 'param'
        # Si param es un string, se asume atributo; si es int, se asume índice
        if isinstance(param, str): # comprueba si param es string
            return getattr(elem, param)() if callable(getattr(elem, param)) else getattr(elem, param) # obtiene el atributo 'param' de 'elem'. Si es un método lo ejecuta mediante la función 'callable'
        else:
            return elem[param] # Si param es int, se asume índice y devuelve el valor en esa posición de elem

    def eliminarminimo(self, param1=None, param2=None): # Elimina el mínimo del montículo
        if self.estavacio()==True: # Si el montículo está vacío, retorna None
            return None
        minimo = self.lista[1] # Guarda el mínimo (primer elemento de la lista)
        self.lista[1] = self.lista[self.tam] # Reemplaza el mínimo con el último elemento de la lista
        self.lista.pop() # Elimina el último elemento de la lista (que ahora se encuentra al inicio)
        self.tam -= 1 # Disminuye el contador de elementos
        self.infiltAbajo(1, param1, param2) # Infiltra el elemento (hacia abajo) desde el inicio de la lista hasta su posición
        return minimo # Retorna el mínimo eliminado

    def infiltAbajo(self, i, param1=None, param2=None): # Infiltra el elemento hacia abajo en el montículo
        if param1 is None or param2 is None: # Si no se especifican parámetros, se usa el comportamiento original (basandose en el valor 'i')
            while (i * 2) <= self.tam: # Comprueba si el elemento tiene un hijo (no es hoja)
                hijo = i * 2 # Calcula el índice del hijo izquierdo
                if hijo + 1 <= self.tam and self.lista[hijo + 1] < self.lista[hijo]: # Comprueba si el hijo derecho existe y es menor que el hijo izquierdo
                    hijo = hijo + 1 # Si es así, se actualiza el índice del hijo al derecho
                if self.lista[hijo] < self.lista[i]: # Comprueba si el hijo es menor que el elemento actual
                    self.lista[i], self.lista[hijo] = self.lista[hijo], self.lista[i] # Intercambia el elemento con su hijo
                    i = hijo # Actualiza el índice del elemento a su nueva posición
                else:
                    break # Si el hijo no es menor, se detiene el proceso (el elemento ya está en su posición)
        else: # Si se especifican parámetros, se usa el comportamiento modificado (basandose en los parametros especificados)
            while (i * 2) <= self.tam: # Comprueba si el elemento tiene un hijo (no es hoja)
                hijo = i * 2 # Calcula el índice del hijo izquierdo
                if hijo + 1 <= self.tam and self._comparar(self.lista[hijo + 1], self.lista[hijo], param1, param2): # Comprueba si el hijo derecho existe y es menor que el hijo izquierdo
                    hijo = hijo + 1 # Si es así, se actualiza el índice del hijo al derecho
                if self._comparar(self.lista[hijo], self.lista[i], param1, param2): # Llama a la función de comparación
                    self.lista[i], self.lista[hijo] = self.lista[hijo], self.lista[i] # Intercambia
                    i = hijo # Actualiza el índice del elemento a su nueva posición
                else:
                    break # Si el hijo no es menor, se detiene el proceso (el elemento ya está en su posición)

    def buscarminimo(self):
        if self.tam == 0: # Si el montículo está vacío, retorna None
            return None
        return self.lista[1] # Retorna el primer elemento de la lista, que es el mínimo en un montículo mínimo
   
    def estavacio(self): # Comprueba si el montículo está vacío
        return self.tamano() == 0 

    def tamano(self): # Retorna el tamaño del montículo
        return self.tam
    
    def construirMonticulo(self,lista): # Construye un montículo a partir de una lista de datos
        monticulo_nuevo = self
        for dato in lista:
            monticulo_nuevo.insertar(dato)
        return monticulo_nuevo
    
    
        
if __name__ == "__main__":
    monticulo = monticulo()
    monticulo.insertar(5)
    monticulo.insertar(3)
    monticulo.insertar(8)
    monticulo.insertar(1)
    monticulo.insertar(4)
    print(monticulo.lista)  # Output: [None, 1, 3, 4, 5, 8]
    print(monticulo.buscarminimo())  # Output: 1
    monticulo.eliminarminimo()
    print(monticulo.lista)  # Output: [None, 3, 4, 5, 8]
    monticulo_nuevo = monticulo.construirMonticulo([7, 2, 6, 4, 1])
    print(monticulo_nuevo.lista)  # Output: [None, 1, 2, 6, 4, 7]
    print(monticulo.tamano())  # Output: 4