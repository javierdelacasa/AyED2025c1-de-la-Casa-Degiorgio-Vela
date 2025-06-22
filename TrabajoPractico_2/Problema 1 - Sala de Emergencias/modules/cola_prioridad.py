from monticulo_min import monticulo


class ColaPrioridad(monticulo): # Clase ColaPrioridad que hereda de la clase monticulo
    def __init__(self):
        self.mont = monticulo() # Inicializa un objeto monticulo para manejar la cola de prioridad
    
    def entrada(self, dato, param1=None, param2=None): # Método para insertar un dato en la cola de prioridad
        self.mont.insertar(dato, param1, param2)

    def salida(self, param1=None, param2=None): # Método para eliminar el elemento con mayor prioridad (mínimo) de la cola
        return self.mont.eliminarminimo(param1, param2)

    def frente(self): # Método para obtener el elemento con mayor prioridad (mínimo) sin eliminarlo
        return self.mont.buscarminimo()

    def tamano(self): # Método para obtener el tamaño de la cola de prioridad
        return self.mont.tamano()
    
    def mostrar_elementos(self): # Método para mostrar los elementos de la cola de prioridad
        for i in range(1, self.tamano()):
            print(self.mont.lista[i])

    def __len__(self): # Método para obtener el tamaño de la cola de prioridad utilizando la función len()
        return self.mont.tamano()
    
    def __iter__(self): # Método para iterar sobre los elementos de la cola de prioridad
        for i in range(1, self.mont.tamano() + 1):
            yield self.mont.lista[i]