from monticulo_min import monticulo

class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}
        self.distancia = float('inf')  # Inicialmente, la distancia es infinita
        self.predecesor = None  # Predecesor en el camino más corto

    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtener_adyacentes(self):
        return self.conectadoA.keys()
    
    def obtenerconectados(self):
        return self.conectadoA

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]
    
    def asignar_distancia(self, distancia):
        self.distancia = distancia

    def obtener_distancia(self):
        return self.distancia
    
    def asignar_predecesor(self, predecesor):   
        self.predecesor = predecesor

    def obtener_predecesor(self):  
        return self.predecesor
    
    

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())

    def existe_vertice(self, vertice):
        return vertice.id in [v for v in self.listaVertices]
    
    def obtenerAristas(self):
        aristas = []
        for v in self.listaVertices.values():
            for vecino, ponderacion in v.obtenerconectados().items():
                aristas.append((v.obtenerId(), vecino.obtenerId(), ponderacion))
        return aristas


def prim (G, inicio):
    cp = monticulo()
    for v in G:
        v.asignar_distancia(float("inf")) #no es el costo entre vertice, es un valor infinito de referencia
        v.asignar_predecesor(None)
    inicio.asignar_distancia(0)
    cp.construirMonticulo([v for v in G], param1="obtener_distancia")
    while not cp.estavacio():
        vertice_actual = cp.eliminarminimo(param1='obtener_distancia')
        for siguiente in vertice_actual.obtener_adyacentes():
            nuevo_costo = vertice_actual.obtenerPonderacion(siguiente)
            if siguiente in cp and nuevo_costo < siguiente.obtener_distancia():
                siguiente.asignar_distancia(nuevo_costo)
                siguiente.asignar_predecesor(vertice_actual)
                cp.decrementar_clave(siguiente, nuevo_costo)

def distanciatotal(G):
    total = 0
    for v in G:
        if v.obtener_predecesor() is not None:
            total += v.obtener_distancia()
    return total

def predecesores_sucesores_aldeas(G):
    for v in G:
        sucesores=[]
        predecesor = v.obtener_predecesor()
        for posibles_sucesores in G:
            if posibles_sucesores.obtener_predecesor() == v:
                posibles_sucesores = posibles_sucesores.obtenerId()
                sucesores.append(posibles_sucesores)
        if not predecesor:
            print(f"La aldea {v.obtenerId()} empieza el recorrido y debe enviar réplicas a {', '.join(sucesores[:-1])} y {sucesores[-1]}")
        elif len(sucesores) == 0:
            print(f"La aldea {v.obtenerId()} recibe el mensaje desde {predecesor.obtenerId()} y no debe enviar réplicas")
        elif len(sucesores) == 1:    
            print(f"La aldea {v.obtenerId()} recibe el mensaje desde {predecesor.obtenerId()} y debe enviar réplicas a {sucesores[0]}")
        else:
            print(f"La aldea {v.obtenerId()} recibe el mensaje desde {predecesor.obtenerId()} y debe enviar réplicas a {', '.join(sucesores[:-1])} y {sucesores[-1]}")
               
        
            
            
            
if __name__ == "__main__":
    g = Grafo()
    for i in range(0,8):
        g.agregarVertice(i)

    g.agregarArista(0,4,8)
    g.agregarArista(4,0,8)
    g.agregarArista(3,0,8)
    g.agregarArista(0,3,8)
    g.agregarArista(3,5,1)
    g.agregarArista(5,3,1)
    g.agregarArista(3,7,6)
    g.agregarArista(7,3,6)
    g.agregarArista(7,6,1)
    g.agregarArista(6,7,1)
    g.agregarArista(7,4,1)
    g.agregarArista(4,7,1)
    g.agregarArista(5,2,8)
    g.agregarArista(2,5,8)
    g.agregarArista(2,1,1)
    g.agregarArista(1,2,1)
    g.agregarArista(2,6,6)
    g.agregarArista(6,2,6)

    prim(g, g.obtenerVertice(3))
    print("Árbol de expansión mínima:")
    for v in g:
        if v.obtener_predecesor() is not None:
            print(f"{v.obtener_predecesor().obtenerId()} - {v.obtenerId()} con costo {v.obtener_distancia()}")

    print(f"La distancia total es: {distanciatotal(g)}")
