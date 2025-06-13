from monticulo_min import monticulo


class ColaPrioridad(monticulo):
    def __init__(self):
        self.mont = monticulo()
    
    def entrada(self, dato, param1=None, param2=None):
        self.mont.insertar(dato, param1, param2)

    def salida(self, param1=None, param2=None):
        return self.mont.eliminarminimo(param1, param2)

    def frente(self):
        return self.mont.buscarminimo()

    def tamano(self):
        return self.mont.tamano()
    
    def mostrar_elementos(self):
        for i in range(1, self.tamano()):
            print(self.mont.lista[i])

    def __len__(self):
        return self.mont.tamano()
    
    def __iter__(self):
        for i in range(1, self.mont.tamano() + 1):
            yield self.mont.lista[i]