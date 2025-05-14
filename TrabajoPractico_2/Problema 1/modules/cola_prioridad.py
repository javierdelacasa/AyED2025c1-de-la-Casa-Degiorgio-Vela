from monticulo_min import monticulo
from paciente import Paciente


class ColaPrioridad(monticulo):
    def __init__(self):
        self.mont = monticulo()
    
    def llegada_de_paciente(self, paciente, param1= 'get_riesgo', param2= 'get_llegada'):
        self.mont.insertar(paciente, param1, param2)

    def atender_paciente(self, param1= 'get_riesgo', param2= 'get_llegada'):
        return self.mont.eliminarminimo(param1, param2)

    def paciente_al_frente(self):
        return self.mont.buscarminimo()

    def pacientes_en_cola(self):
        return self.mont.tamano()
    
    def mostrar_pacientes(self):
        for i in range(1, self.tamano()):
            print(self.mont.lista[i])

    def __len__(self):
        return self.mont.tamano()
    
    def __iter__(self):
        for i in range(1, self.mont.tamano() + 1):
            yield self.mont.lista[i]