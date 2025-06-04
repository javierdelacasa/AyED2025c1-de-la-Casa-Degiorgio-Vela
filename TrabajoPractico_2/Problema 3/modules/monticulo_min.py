class monticulo():
    def __init__(self):
        self.lista = [None]
        self.tam = 0
    
    def _obtener_valor(self, elem, param):
        # Si param es un string, se asume atributo; si es int, se asume índice
        if isinstance(param, str):
            return getattr(elem, param)() if callable(getattr(elem, param)) else getattr(elem, param)
        else:
            return elem[param]

    def _comparar(self, a, b, param1, param2):
        v1a = self._obtener_valor(a, param1)
        v1b = self._obtener_valor(b, param1)
        if v1a < v1b:
            return True
        elif v1a == v1b:
            return True #no importa el segundo parametro
        else:
            return False

    def infiltArriba(self, i, param1=None, param2=None):
        if param1 is None and param2 is None:
            # Comportamiento original (por valor directo)
            while i // 2 > 0:
                if self.lista[i] < self.lista[i // 2]:
                    self.lista[i], self.lista[i // 2] = self.lista[i // 2], self.lista[i]
                i = i // 2
        else:
            while i // 2 > 0:
                if self._comparar(self.lista[i], self.lista[i // 2], param1, param2):
                    self.lista[i], self.lista[i // 2] = self.lista[i // 2], self.lista[i]
                i = i // 2

    def infiltAbajo(self, i, param1=None, param2=None):
        if param1 is None and param2 is None:
            # Comportamiento original (por valor directo)
            while (i * 2) <= self.tam:
                hijo = i * 2
                if hijo + 1 <= self.tam and self.lista[hijo + 1] < self.lista[hijo]:
                    hijo = hijo + 1
                if self.lista[hijo] < self.lista[i]:
                    self.lista[i], self.lista[hijo] = self.lista[hijo], self.lista[i]
                    i = hijo
                else:
                    break
        else:
            while (i * 2) <= self.tam:
                hijo = i * 2
                if hijo + 1 <= self.tam and self._comparar(self.lista[hijo + 1], self.lista[hijo], param1, param2):
                    hijo = hijo + 1
                if self._comparar(self.lista[hijo], self.lista[i], param1, param2):
                    self.lista[i], self.lista[hijo] = self.lista[hijo], self.lista[i]
                    i = hijo
                else:
                    break
    
    def insertar(self,dato,param1=None, param2=None):
        self.lista.append(dato)
        self.tam = self.tam + 1
        self.infiltArriba(self.tam, param1, param2)

    def buscarminimo(self):
        if self.tam == 0:
            return None
        return self.lista[1]
    
    def eliminarminimo(self, param1=None, param2=None):
        if self.estavacio()==True:
            return None
        minimo = self.lista[1]
        self.lista[1] = self.lista[self.tam]
        self.lista.pop()
        self.tam -= 1
        self.infiltAbajo(1, param1, param2)
        return minimo

    def estavacio(self):
        return self.tamano() == 0

    def tamano(self):
        return self.tam
    
    def construirMonticulo(self,lista,param1=None, param2=None):
        monticulo_nuevo = self
        for dato in lista:
            monticulo_nuevo.insertar(dato, param1, param2)
        return monticulo_nuevo
    
    def __in__(self, dato):
        return dato in self.lista
    
    def decrementar_clave(self, dato, nuevo_valor):
    # Busca el índice del dato y actualiza su posición
        for i in range(1, self.tam + 1):
            if self.lista[i] == dato:
                # Actualiza el valor antes de reordenar
                dato.asignar_distancia(nuevo_valor)
                self.infiltArriba(i, "obtener_distancia", "obtenerId")
                break

    def __iter__(self):
        return iter(self.lista[1:]) 
    
        
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