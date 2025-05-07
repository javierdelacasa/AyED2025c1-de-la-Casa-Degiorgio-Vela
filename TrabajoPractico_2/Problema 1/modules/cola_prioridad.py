from monticulo_min import monticulo
from modules.paciente import paciente


class ColaPrioridad(monticulo):
    def __init__(self):
        self = monticulo()
    
    def llegada_de_paciente(self, paciente):
        self.insertar(paciente)

    def atender_paciente(self):
        self.eliminarminimo()

    def paciente_al_frente(self):
        return self.buscarminimo()

    def pacientes_en_cola(self):
        return self.tamano()
    
    def mostrar_pacientes(self):
        for i in range(1, self.tamano()):
            print(self.lista[i])

    