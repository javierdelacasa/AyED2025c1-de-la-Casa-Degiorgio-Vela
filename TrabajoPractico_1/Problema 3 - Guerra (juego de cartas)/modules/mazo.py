
from LDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada
from carta import Carta  # Importa la clase Carta

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self.lista= ListaDobleEnlazada()
    def poner_carta_arriba(self,carta):
        self.lista.agregar_al_inicio(carta)
    def sacar_carta_arriba(self):
        if self.lista.esta_vacia():
            raise DequeEmptyError("El mazo está vacío")
        self.lista.cabeza.dato.visible = True  # Asegúrate de que `dato` tiene el atributo `visible`
        temp = self.lista.cabeza.dato
        self.lista.extraer(0)
        return temp
            


if __name__ == "__main__":
    mazo = Mazo()
    carta1 = Carta("♣", "3")
    carta2 = Carta("♦", "A")
    carta3 = Carta("♣", "8")
    
    
    mazo.poner_carta_arriba(carta1)
    mazo.poner_carta_arriba(carta2)
    mazo.poner_carta_arriba(carta3) 
    
    
    print(mazo.sacar_carta_arriba())
    print(mazo.sacar_carta_arriba())  # Debería imprimir la carta en la parte superior del mazo
