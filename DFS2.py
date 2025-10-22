import grafos as gf
from queue import LifoQueue

grafo = gf.grafo


def DFS(grafo, Vinicio, Vfinal):
    
    frontier = LifoQueue() 
    frontier.put(Vinicio)
    
    #en vez de una lista se usó en diccionario para ver las naciones exploradas para manejarlo por nombres (de naciones) y no por posiciones, ya que sigue la misma logica de las siguientes instrucciones y sería mas facil manejarlo
    explored_set = {nacion: False for nacion in grafo} 
    explored_set[Vinicio] = True
    parents = {Vinicio: None}
    
    while True:
        
        if frontier.empty():
            return None
        
        Vcurrent = frontier.get()
        if Vcurrent == Vfinal:
            path = []
            
            while Vcurrent is not None: #Se repite el proceso para guardar a los padres del nodo, como el nodo iniciaol no tiene parientes (null), sabemos que ahi se tiene que detener el proceos
                path.append(Vcurrent)
                Vcurrent = parents[Vcurrent]
            return list(reversed(path)) #Se regresa el resultado en forma de lista, pero invertida, ya que la manera que se va añadiendo a la lista los parientes es al revés
        
        for v in grafo[Vcurrent]:
            if not explored_set[v]:
                frontier.put(v)  
                explored_set[v] = True  
                parents[v] = Vcurrent  
                


print("Camino DFS de Goding a Naphia: ", DFS(grafo, "Goding", "Niaphia"), "\n") #Imprime el camino de Goding hasta Niaphia
print("Camino DFS de Zrusall a Blebus: ",DFS(grafo, "Zrusall", "Blebus"), "\n")
print("Camino DFS de Lagos a Goding: ",DFS(grafo, "Lagos", "Goding"), "\n")
print("Camino DFS de Goxmont a Ontdale: ",DFS(grafo, "Goxmont", "Ontdale"), "\n")
        
