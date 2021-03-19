import sys
from Estaciones import linea1,linea2,linea3,linea4,linea5,linea6,linea7,linea8,linea9,lineaA,lineaB,linea12,lineas
import os
import tkinter as tk


class StdOutRedirect:
    def __init__(self,  text: tk.Text) -> None:
        self._text = text

    def write(self,  out: str) -> None:
        self._text.insert(tk.END,  out)

class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent,  *args, **kwargs)
        self.stdout_text = tk.Text(
            self,  bg="black",  fg="#38B179",  font=("Helvetica", 15))
        self.stdout_text.pack(expand=True, fill=tk.BOTH)
        sys.stdout = StdOutRedirect(self.stdout_text)

class Vertice(): 
    def __init__(self, nombre):         
        self.nombre = nombre            
        self.vecinos = []               
        self.distancia = sys.maxsize     
        self.color = ""              
        self.padre = None               

    def AgregarVecino(self, vertice): 
        if vertice in self.vecinos:
            return
        
        self.vecinos.append(vertice)

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre

class Grafo():

    def __init__(self):
        self.vertices = {}

    def AgregarVertice(self, nombreVertice):
        if nombreVertice in self.vertices: 
            return False

        vertice = Vertice ( nombreVertice )

        self.vertices[vertice.nombre] = vertice
        return True

    def AgregarArista(self, verticeNombre1, verticeNombre2):
        if verticeNombre1 in self.vertices and verticeNombre2 in self.vertices:

            vertice1 = self.vertices[verticeNombre1]
            vertice2 = self.vertices[verticeNombre2]

            vertice1.AgregarVecino(vertice2)
            vertice2.AgregarVecino(vertice1)
            return True
        else:
            return False

    def BFS( self, nombreStart ):                  
        for u in self.vertices.values():
            u.color = "blanco"
            u.distancia = sys.maxsize
            u.padre = None

        verticeStart = self.vertices[nombreStart]
        verticeStart.color = "gris"
        verticeStart.distancia = 0
        verticeStart.padre = None

        cola = []

        cola.append( verticeStart )

        while len(cola) != 0:
            u = cola.pop( 0 )
            for v in u.vecinos:
                if v.color == "blanco":
                    v.color = "gris"
                    v.distancia = u.distancia + 1
                    v.padre = u
                    cola.append( v )

            u.color = "negro"
    
    def DFS(self,nombreVerticeInicial):
        for vertice in self.vertices.values():
            vertice.color = "blanco"
            vertice.padre = None
            vertice.distancia = sys.maxsize
        
        verticeInicial = self.vertices[nombreVerticeInicial]
        verticeInicial.color = "gris"
        verticeInicial.distancia = 0

        self.DFSVisitar(verticeInicial)

    def DFSVisitar(self,vertice):
        vertice.color = "gris"
        for v in vertice.vecinos:
            if v.color == "blanco" :
                v.padre = vertice
                v.color = "gris"
                v.distancia = vertice.distancia + 1
                self.DFSVisitar(v)
            
            v.color = "negro"


    def ImprimirRutaDFS(self,verticeInicial, verticeFinal):
        self.DFS(verticeInicial)

        ruta =[]
        verticeActual = self.vertices[verticeFinal]
        while verticeActual is not None:
            ruta.append(verticeActual)
            verticeActual = verticeActual.padre
        print(*ruta[::-1], sep=" -> ")

    def ImprimirRutaBFS(self,verticeInicial, nombreVerticeFinal):
        self.BFS(verticeInicial)

        ruta = []
        verticeActual = self.vertices[nombreVerticeFinal]
        while verticeActual is not None:
            ruta.append(verticeActual)
            verticeActual = verticeActual.padre
        print(*ruta[::-1], sep=" -> ")


    def __str__(self):
        s = ""
        for nombreVertice in self.vertices.keys():
            s = s + nombreVertice + " " +  " -> " + str(self.vertices[nombreVertice].vecinos) + "\n"
        return s

def busquedaLineal():
    for i in range(len(A)):
        if A[i] == Key:
            return i
    return -1

def llamarBusqueda():
    estacion = entrada_estacion.get()
    Key = estacion
    resultado = busquedaLineal(lineas, Key)
    print("La estación esta en la línea: " + lineas)

def mainM():
    root = tk.Tk()
    App(root).pack(expand=True, fill=tk.BOTH)

    archivo1 = open("estacion_destino.txt", "r")
    estacion_destino = archivo1.read()
    archivo1.close()

    archivo2 = open("estacion_inicial.txt", "r")
    estacion_inicial = archivo2.read()
    archivo2.close()

    graph = Grafo()
    estaciones = []
    for i in range(len(lineas)): 
        estaciones = lineas[i]
        for u in range(len(estaciones)):
            graph.AgregarVertice(estaciones[u])
        
    for i in range(len(lineas)): 
            estaciones = lineas[i]
            for u in range(len(estaciones)):
                if u + 1 < len(estaciones):
                    graph.AgregarArista(estaciones[u] , estaciones[u + 1])

    print("\tImprimiendo ruta mas optima BFS para " + estacion_inicial + " y " + estacion_destino + "\n")

    graph.ImprimirRutaBFS(estacion_inicial, estacion_destino)
        
    print("\n\tImprimiendo ruta mas optima DFS para " + estacion_inicial + " y " + estacion_destino + "\n")

    graph.ImprimirRutaDFS(estacion_inicial, estacion_destino)
    root.mainloop()
    
if __name__ == "__main__":
    mainM()
    
    
