import numpy as np
import math as mt
import grafos as gf

grafo = gf.grafo

def convert(grafo):#Fue necesario hacer una funcion para convertir de un diccionario a una matriz de adyacencia
    nodos = list(grafo.keys())
    n = len(nodos)
    matriz = np.zeros((n, n))

    for i, nodo in enumerate(nodos):
        for vecino, peso in grafo[nodo].items():
            j = nodos.index(vecino)
            matriz[i][j] = peso

    return nodos, matriz

# Algoritmo Floyd-Warshall
def floyd_warshall(matriz):
    BIG_NUMBER = mt.inf
    n = len(matriz)
    matrix = [[matriz[i][j] if matriz[i][j] != 0 else BIG_NUMBER for j in range(n)] for i in range(n)]#Se reemplazan los 0 por infinitos (BIG_NUMBER)
    for i in range(n):
        matrix[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    return matrix

# Ejecución
nodos, matriz = convert(grafo) #EL primer valor que regresa la funcion son los nodos, y despues la matriz de aydacencia
distancias = floyd_warshall(matriz)#Algoritmo de floyd


#inicio = i
#destino = j
#Ejemplo distancias[origen][destino]
print("Distancia minima de Goding a Niaphia", distancias[10][4]) #posiciones de origne y destino de nuestro grafo
print("Distancia minima de Zrusall a Blebus: ", distancias[2][7]) #2 = Zrusall 7 = Blebus
print("Distancia minima de Lagos a Goding: ",distancias[5][10]) #5 = Lagos 10 = Goding
print("Camino DFS de Goxmont a Ontdale: ", distancias[3][9])#3 = Goxmont  9 = Ontdale
