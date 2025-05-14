# -*- coding: utf-8 -*-

from random import randint, choices
from datetime import datetime

nombres = ['Eduardo', 'Javier', 'Santiago', 'Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Degiorgio', 'De la Casa', 'Vela', 'Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__llegada = datetime.now()

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion

    def get_llegada(self):
        return self.__llegada
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion + '\t -> '
        cad += self.__llegada.strftime("%Y-%m-%d %H:%M:%S")
        return cad
        
if __name__ == "__main__":
    p = Paciente()
    print(p)
    print(p.get_nombre())
    print(p.get_apellido())
    print(p.get_riesgo())
    print(p.get_descripcion_riesgo())
    print(p.get_llegada())
    print(p.__str__())
        