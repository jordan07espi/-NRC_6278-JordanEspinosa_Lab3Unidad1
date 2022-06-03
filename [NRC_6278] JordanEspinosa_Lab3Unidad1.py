#BÚSQUEDAS POR AMPLITUD
#Importamos la librería Queue
from queue import Queue
#Se crea la clase Grafo
class Grafo:
    """
    Clase que identifica a un grafo.
    ...
    Atributos
    ---------
    numero_de_nodos : int
        número de nodos
    dirigido: boolean
        grafo dirigido
    
    Métodos
    -------
    agregar_arista(nodo1, nodo2, peso=1):
        Agregar arista al grafo.
    
    imprimir_lista_adyacencia():
        Imprime la lista de adyacencia.
    
    bfs_traversal(inicio_nodo):
        Recorre el grafo.
    """
    # Constructor
    def _init_(self, numero_de_nodos, dirigido=True):
        """
        Construye todos los atributos necesarios para el objeto grafo.
        Parámetros:
        ----------
            numero_de_nodos: int
                Número de nodos del grafo
            dirigido: boolean
                Grafo dirigido o No dirgido
        """
        #Número de nodos
        self.m_numero_de_nodos = numero_de_nodos
        #Rango del número de nodos
        self.m_nodos = range(self.m_numero_de_nodos)
        # Especifica si es dirigido o no dirigido
        self.m_dirigido = dirigido
        # Representación gráfica - Lista de adyacencia
        # Utilizamos un diccionario para implementar una lista de adyacencia
        self.m_lista_adyacencia = {node: set() for node in self.m_nodos}#Setea los nodos mediante un ciclo de repetición      
	
    # Agrega una arista al grafo
    def agregar_arista(self, nodo1, nodo2, peso=1):
        """
        Agrega una arista al grafo.
        Pasa al siguiente grafo si el primero no se encuentra dirigido
        Parámetros:
        ----------
        nodo1: int
            Nodo 1 - Inicio
        nodo1: int
            Nodo 2 - Fin
        peso: int
            Peso de la arista
        """
        #Añade una arista al nodo 1 para la lista del grafo
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        #Se añáde al otro nodo una arista si grafo resulta no estar dirigido
        if not self.m_dirigido:
            #Añade una arista al nodo 2 para la lista del grafo
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))
    
    # Imprime la representación del grafo
    def imprimir_lista_adyacencia(self):
        '''Imprime la lista de adyacencia'''
        #Recorrido en la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            #Imprime los nodos que estan en la lista de adyacencia
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])


    # Función que imprime el recorrido DFS
    def dfs(self, inicial, objetivo, camino = [], visitado = set()):
        '''
        Método que realiza un recorrido del grafo por profundidad
                
            Parámetros:
            ----------
            inicial : int 
                    Nodo de inicio
            objetivo : int
                    Nodo de fin
            visitado: list
                    Conjunto vacío de nodos visitados
            camino : list
                    Lista vacia
            Returns:
                camino : list
                    Lista del camino recorrido
                resultado: list
                    resultado del par ordenado
        '''
        
        # Agrega el nodo inicial a la lista camino
        camino.append(inicial)
        # Agrega el nodo inicial al lista visitado
        visitado.add(inicial)
        # Si el inicial es igual al objetivo termina su recorrido
        #Finaliza el programa
        if inicial == objetivo:
            # Retorna la lista camino
            return camino
        #Recorre el nodo vecino del inicio de lista de adyacencia
        for (vecino, peso) in self.m_lista_adyacencia[inicial]:
            #Verifica que el nodo vecino no se ha visitado
            if vecino not in visitado:
                #Preguntar si es igual al objetivo
                resultado = self.dfs(vecino, objetivo, camino, visitado)
                #Resultado no es ninguna
                if resultado is not None:
                    #Devuelve el par ordenado
                    return resultado
        # Elimina y retorna un elemento de la lista de camino
        camino.pop()
        #No hay valor posible que devolver
        return None

#Función Main de la clase
if _name_ == "_main_":
    '''
        Main de la clase Grafo
        Imprime los nodos nodos asignados y muestra el camino recorrido
        
    '''
    # Crea una instancia de la clase "Grafo"
    # Este grafo es no dirigido y tiene 5 nodos
    g = Grafo(5, dirigido=False)
    
    # Agrega las aristas del grafo
    # Añáde las aristas (0,1)
    g.agregar_arista(0,1)
    # Añáde las aristas (0,2)
    g.agregar_arista(0,2)
    # Añáde las aristas (1,3)
    g.agregar_arista(1,3)
    # Añáde las aristas (2,3)
    g.agregar_arista(2,3)
    # Añáde las aristas (3,4)
    g.agregar_arista(3,4)
    
    # Imprime la lista de adyacencia
    g.imprimir_lista_adyacencia()
    
    # lista vacía del camino del recorrido
    camino_recorrido = []
    # Se intancia el camino del recorrido
    # desde el nodo 0 al nodo 3
    camino_recorrido = g.dfs(0, 3)
    # Imprime el camino del recorrido
    print(f" El camino del recorrido del nodo 0 al nodo 3 es {camino_recorrido}")
    #Imprime la documentanción
    help(Grafo)