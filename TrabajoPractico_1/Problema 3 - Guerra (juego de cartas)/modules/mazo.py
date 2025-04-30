
from modules.LDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada
from modules.carta import Carta  # Importa la clase Carta

class DequeEmptyError(Exception):
    """Excepción personalizada para indicar que el mazo está vacío."""
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self.lista= ListaDobleEnlazada()
    def poner_carta_arriba(self,carta):
        self.lista.agregar_al_inicio(carta)
    def sacar_carta_arriba(self,mostrar=False):
        if self.lista.esta_vacia():
            raise DequeEmptyError("El mazo está vacío")
        if mostrar == True:
            self.lista.cabeza.dato.visible = True  # Asegúrate de que `dato` tiene el atributo `visible`
        temp = self.lista.cabeza.dato
        self.lista.extraer(0)
        return temp
    def poner_carta_abajo(self,carta):
        self.lista.agregar_al_final(carta)
    def __len__(self):
        return len(self.lista)


if __name__ == "__main__":
    mazo = Mazo()
    carta1 = Carta("♣", "3")
    carta2 = Carta("♦", "A")
    carta3 = Carta("♣", "8")
    
    
    mazo.poner_carta_arriba(carta1)
    mazo.poner_carta_arriba(carta2)
 #   mazo.poner_carta_arriba(carta3) 
    
    
    print(mazo.sacar_carta_arriba())
    print(mazo.sacar_carta_arriba())  # Debería imprimir la carta en la parte superior del mazo
