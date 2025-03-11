class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        # Creamos una copia de la lista para no modificar la original
        lista_copia = lista.copy()
        # Obtenemos los índices de inicio y fin
        izquierda = 0
        derecha = len(lista_copia) - 1
        
        # Intercambiamos elementos desde los extremos hacia el centro
        while izquierda < derecha:
            # Intercambiamos los elementos en las posiciones izquierda y derecha
            lista_copia[izquierda], lista_copia[derecha] = lista_copia[derecha], lista_copia[izquierda]
            izquierda += 1
            derecha -= 1
        
        return lista_copia
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        if not lista:
            return -1
        for i in range (len(lista)):
            if lista[i]==elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        elim_duplicado = []
        elementos_vistos = []
        for elemento in lista:
            if (elemento, type(elemento)) not in elementos_vistos:
                elim_duplicado.append(elemento)
                elementos_vistos.append((elemento, type(elemento)))
        return elim_duplicado
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        resultado = []
        i = 0  # Índice para lista1
        j = 0  # Índice para lista2
        
        # Combinamos ambas listas mientras haya elementos en ambas
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        
        # Agregamos los elementos restantes de lista1, si los hay
        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1
        
        # Agregamos los elementos restantes de lista2, si los hay
        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1
        
        return resultado
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not lista:
            return []
        x = x % len(lista)
        return lista[-x:] + lista[ :-x] 
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        n = len(lista) + 1  # Longitud esperada + 1 (por el número faltante)
        suma_esperada = (n * (n + 1)) // 2  # Suma de 1 a n+1
        suma_actual = sum(lista)
        return suma_esperada - suma_actual
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pila = {"_top": -1, "_stack": []}

        def push(elemento):
            pila["_top"] += 1
            pila["_stack"].append(elemento)

        def peek():
            if pila["_top"] >= 0:
                return pila["_stack"][pila["_top"]]
            return None

        def pop():
            if pila["_top"] >= 0:
                elemento = pila["_stack"][pila["_top"]]
                pila["_stack"].pop()
                pila["_top"] -= 1
                return elemento
            return None

        def is_empty():
            return pila["_top"] < 0

        return {
            "push": push,
            "peek": peek,
            "pop": pop,
            "is_empty": is_empty
        }
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        cola = {"_queue": []}

        def enqueue(elemento):
            cola["_queue"].append(elemento)

        def dequeue():
            if cola["_queue"]:
                return cola["_queue"].pop(0)
            return None

        def peek():
            if cola["_queue"]:
                return cola["_queue"][0]
            return None

        def is_empty():
            return len(cola["_queue"]) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        if not matriz:
            return []
        
        # Obtener dimensiones de la matriz
        filas = len(matriz)
        if filas == 0:
            return []
        columnas = len(matriz[0])
        
        # Crear una nueva matriz transpuesta
        transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]
        
        # Llenar la matriz transpuesta
        for i in range(filas):
            for j in range(columnas):
                transpuesta[j][i] = matriz[i][j]
        
        return transpuesta