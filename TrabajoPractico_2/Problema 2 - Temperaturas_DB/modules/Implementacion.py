from modules.AVL import Arbol
import datetime

class Temperatura_DB():
    def __init__(self):
        self.arbol = Arbol() # Crea un arbol AVL para almacenar las temperaturas
    
    def convertir_fecha(self, fechastr): # Convierte una fecha en formato string a un objeto datetime
        if isinstance(fechastr, str):
            fecha = datetime.datetime.strptime(fechastr, "%d/%m/%Y")
            return fecha

    def guardar_temperatura(self, temperatura, fechastr=None):
        if fechastr is None: # Si no se proporciona una fecha, se usa la fecha actual
            fechastr = datetime.datetime.now().strftime("%d/%m/%Y")
        elif isinstance(fechastr, datetime.datetime): # Si se proporciona un objeto datetime, se convierte a string
            fechastr = fechastr.strftime("%d/%m/%Y")
        fecha = self.convertir_fecha(fechastr) 
        self.arbol.agregar(fecha, temperatura) # Agrega al arbol con la fecha como clave

    def devolver_temperatura(self, fechastr):
        fecha = self.convertir_fecha(fechastr) # Convierte la fecha a datetime
        return self.arbol.obtener(fecha)
    
    def max_temp_rango(self, fecha_iniciostr, fecha_finstr):
        fecha_inicio = self.convertir_fecha(fecha_iniciostr)
        fecha_fin = self.convertir_fecha(fecha_finstr)

        return self.arbol.obtenermaximo_rango(fecha_inicio, fecha_fin)[1] # Devuelve la carga util de la tupla obtenida
    
    def min_temp_rango(self, fecha_iniciostr, fecha_finstr):
        fecha_inicio = self.convertir_fecha(fecha_iniciostr)
        fecha_fin = self.convertir_fecha(fecha_finstr)

        return self.arbol.obtenerminimo_rango(fecha_inicio, fecha_fin)[1] # Devuelve la carga util de la tupla obtenida
    
    def temp_extemos_rango(self, fecha_iniciostr, fecha_finstr):
        fecha_inicio = self.convertir_fecha(fecha_iniciostr)
        fecha_fin = self.convertir_fecha(fecha_finstr)

        # Utiliza las funciones obtenermaximo_rango y obtenerminimo_rango del arbol AVL
        max_temp = self.arbol.obtenermaximo_rango(fecha_inicio, fecha_fin)[1]
        min_temp = self.arbol.obtenerminimo_rango(fecha_inicio, fecha_fin)[1]
        return (max_temp, min_temp)
    
    def devolver_todas_temperaturas(self):
        for nodo in self.arbol: # Recorre el arbol AVL y devuelve todas las temperaturas
            print(f"Fecha: {nodo[0].strftime('%d/%m/%Y')}, Temperatura: {nodo[1]} ºC")

    def devolver_temperaturas(self, fecha_iniciostr, fecha_finstr):
        fecha_inicio = self.convertir_fecha(fecha_iniciostr)
        fecha_fin = self.convertir_fecha(fecha_finstr)
        # Recorre el arbol 
        for nod in self.arbol:
            if fecha_inicio <= nod[0] <= fecha_fin: # Verifica si la fecha del nodo está dentro del rango
                print(f"Fecha: {nod[0].strftime('%d/%m/%Y')}, Temperatura: {nod[1]} ºC")

    def cantidad_muestras(self):
        return self.arbol.tamanio()
    
    def borrar_temperatura(self, fechastr):
        fecha = self.convertir_fecha(fechastr)
        self.arbol.eliminar(fecha)
    





    
    