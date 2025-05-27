from AVL import Arbol
import datetime

class Temperatura_DB():
    def __init__(self):
        self.arbol = Arbol()
    
    def guardar_temperatura(self, temperatura):
        fecha = datetime.datetime.now()
        self.arbol.agregar(fecha, temperatura)

    def devolver_temperatura(self, fecha):
        return self.arbol.obtener(fecha)
    
    def max_temp_rango(self, fecha_inicio, fecha_fin):
        return self.arbol.obtenermaximo_rango(fecha_inicio, fecha_fin)[1]
    
    def min_temp_rango(self, fecha_inicio, fecha_fin):
        return self.arbol.obtenerminimo_rango(fecha_inicio, fecha_fin)[1]
    
    def temp_extemos_rango(self, fecha_inicio, fecha_fin):
        max_temp = self.arbol.obtenermaximo_rango(fecha_inicio, fecha_fin)[1]
        min_temp = self.arbol.obtenerminimo_rango(fecha_inicio, fecha_fin)[1]
        return (max_temp, min_temp)
    
    def devolver_todas_temperaturas(self):
        self.arbol.preorden_obtencion()

    def devolver_temperaturas(self, fecha_inicio, fecha_fin):
        self.arbol.preorden_rango_obtencion(fecha_inicio, fecha_fin)

    def cantidad_muestras(self):
        return self.arbol.tamanio()
    

if __name__ == "__main__":
    db = Temperatura_DB()
    db.guardar_temperatura(25.5)
    db.guardar_temperatura(30.2)
    db.guardar_temperatura(22.1)
    db.guardar_temperatura(28.4)
    db.guardar_temperatura(26.3)   
    db.guardar_temperatura(29.0)
    db.devolver_todas_temperaturas()
    print("Temperatura en fecha específica:", db.devolver_temperatura(datetime.datetime.now()))
    fecha_inicio = datetime.datetime.now() - datetime.timedelta(days=5)
    fecha_fin = datetime.datetime.now()
    print("Temperatura máxima en rango:", db.max_temp_rango(fecha_inicio, fecha_fin))
    print("Temperatura mínima en rango:", db.min_temp_rango(fecha_inicio, fecha_fin))
    print("Temperaturas extremas en rango:", db.temp_extemos_rango(fecha_inicio, fecha_fin))
    print("Cantidad de muestras:", db.cantidad_muestras())
    db.devolver_temperaturas(fecha_inicio, fecha_fin)
    print("Temperaturas en rango:")

    db.devolver_temperaturas(fecha_inicio, fecha_fin)

    
    