class monticulo():
    def __init__(self):
        self.lista = [None]
        self.tam = 0

    def infiltArriba(self,i,k=None):
        if k is None:
            while i // 2 > 0:
                if self.lista[i] < self.lista[i // 2]:
                    tmp = self.lista[i // 2]
                    self.lista[i // 2] = self.lista[i]
                    self.lista[i] = tmp
                i = i // 2
        else:
            while i // 2 > 0:
                if self.lista[i][k] < self.lista[i // 2][k]:
                    tmp = self.lista[i // 2][k]
                    self.lista[i // 2][k] = self.lista[i][k]
                    self.lista[i][k] = tmp
                i = i // 2

    def infiltAbajo(self,i,k=None):
        if k is None:
            while (i * 2) <= self.tam:
                if self.lista[i] > self.lista[i * 2]:
                    tmp = self.lista[i * 2]
                    self.lista[i * 2] = self.lista[i]
                    self.lista[i] = tmp
                    i = i * 2
                elif (i * 2 +1) > self.tam:
                    break
                elif self.lista[i] > self.lista[i * 2 + 1]:
                    tmp = self.lista[i * 2 + 1]
                    self.lista[i * 2 + 1] = self.lista[i]
                    self.lista[i] = tmp
                    i = i * 2 + 1
                else:
                    break
        else:
            while (i * 2) <= self.tam:
                if self.lista[i][k] > self.lista[i * 2][k]:
                    tmp = self.lista[i * 2][k]
                    self.lista[i * 2][k] = self.lista[i][k]
                    self.lista[i][k] = tmp
                    i = i * 2
                elif (i * 2 +1) > self.tam:
                    break
                elif self.lista[i][k] > self.lista[i * 2 + 1][k]:
                    tmp = self.lista[i * 2 + 1][k]
                    self.lista[i * 2 + 1][k] = self.lista[i][k]
                    self.lista[i][k] = tmp
                    i = i * 2 + 1
                else:
                    break

    
    def insertar(self,dato):
        self.lista.append(dato)
        self.tam = self.tam + 1
        self.infiltArriba(self.tam)

    def buscarminimo(self):
        if self.tam == 0:
            return None
        return self.lista[1]
    
    def eliminarminimo(self):
        if self.estavacio() == True:
            return None
        self.lista[1] = self.lista[self.tam]
        tmp = self.lista.pop()
        self.tam = self.tam - 1
        self.infiltAbajo(1)
        return tmp

    def estavacio(self):
        return self.tamano() == 0

    def tamano(self):
        return self.tam
    
    def construirMonticulo(self,lista):
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