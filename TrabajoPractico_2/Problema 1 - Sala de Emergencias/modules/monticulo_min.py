class monticulo():
    def __init__(self):
        self.lista = [None] # Crea una lista vacía
        self.tam = 0 # Inicia el contador de elementos
    
    def insertar(self,dato,param1=None, param2=None): # Inserta un elemento en el montículo. De base, sin parámetros
        self.lista.append(dato) # Añade el dato al final de la lista
        self.tam = self.tam + 1 # Aumenta el contador
        self.infiltArriba(self.tam, param1, param2) # Infiltra el elemento desde el final de la lista hasta su posición

    def infiltArriba(self, i, param1=None, param2=None):
        if param1 is None or param2 is None: # Comportamiento original (basandose en el valor 'i')
            while i // 2 > 0: # Comprueba si el elemento no es raíz
                if self.lista[i] < self.lista[i // 2]: # Si es menor al padre
                    self.lista[i], self.lista[i // 2] = self.lista[i // 2], self.lista[i] # Intercambia el elemento con su padre
                i = i // 2 # Actualiza el índice a su nueva posición
        else: # Si se especifican parámetros, se usa el comportamiento modificado
            while i // 2 > 0: 
                if self._comparar(self.lista[i], self.lista[i // 2], param1, param2): # Llama a la función de comparación (comprueba que sea menor al padre)
                    self.lista[i], self.lista[i // 2] = self.lista[i // 2], self.lista[i] # Intercambia el elemento con su padre
                i = i // 2 # Actualiza el índice a su nueva posición

    def _comparar(self, a, b, param1, param2): # Comprueba si 'a' es menor a 'b', con respecto a los parametros especificados
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

    def _obtener_valor(self, elem, param): # Obtiene el valor asociado a un elemento con respecto al parámetro
        if isinstance(param, str): # Si param es string
            return getattr(elem, param)() if callable(getattr(elem, param)) else getattr(elem, param) # Comprueba mediante la función 'callable' si es un método y lo ejecuta, de lo contario lo obtiene directamente
        else:
            return elem[param] # Si param es int, se asume índice y devuelve el valor en esa posición de elem

    def eliminarminimo(self, param1=None, param2=None):
        if self.estavacio()==True: # Si el montículo está vacío, retorna None
            return None
        minimo = self.lista[1] # Guarda el mínimo
        self.lista[1] = self.lista[self.tam] # Reemplaza el mínimo con el último elemento de la lista
        self.lista.pop() # Elimina el último elemento de la lista
        self.tam -= 1 # Disminuye el contador
        self.infiltAbajo(1, param1, param2) # Infiltra el ahora primer elemento hacia abajo
        return minimo # Retorna el mínimo eliminado

    def infiltAbajo(self, i, param1=None, param2=None): 
        if param1 is None or param2 is None: # Comportamiento original (basandose en el valor 'i')
            while (i * 2) <= self.tam: # Mientras el elemento actual no sea hoja
                hijo = i * 2 # Calcula el índice del hijo izquierdo
                if hijo + 1 <= self.tam and self.lista[hijo + 1] < self.lista[hijo]: # Comprueba si el hijo derecho existe y es menor que el hijo izquierdo
                    hijo = hijo + 1 # Se actualiza el índice del hijo al derecho
                if self.lista[hijo] < self.lista[i]: # Si el hijo es menor que el elemento actual
                    self.lista[i], self.lista[hijo] = self.lista[hijo], self.lista[i] # Intercambia el elemento con su hijo
                    i = hijo # Actualiza el índice a su nueva posición
                else:
                    break # Se detiene el proceso (el elemento ya está en su posición)

        else: # Comportamiento modificado (basandose en los parametros especificados)
            while (i * 2) <= self.tam: # Mientras el elemeto actual no sea hoja
                hijo = i * 2 # Calcula el índice del hijo izquierdo
                if hijo + 1 <= self.tam and self._comparar(self.lista[hijo + 1], self.lista[hijo], param1, param2): # Comprueba si el hijo derecho existe y es menor que el hijo izquierdo
                    hijo = hijo + 1 # Se actualiza el índice del hijo al derecho
                if self._comparar(self.lista[hijo], self.lista[i], param1, param2): # Si la funcion comparacion retorna 'True'
                    self.lista[i], self.lista[hijo] = self.lista[hijo], self.lista[i] # Intercambia el elemento con su hijo
                    i = hijo # Actualiza el índice a su nueva posición
                else:
                    break # Se detiene el proceso (el elemento ya está en su posición)

    def buscarminimo(self):
        if self.tam == 0: # Si el montículo está vacío, retorna None
            return None
        return self.lista[1] # Retorna el primer elemento de la lista, que es el mínimo en un montículo de mínimos
   
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