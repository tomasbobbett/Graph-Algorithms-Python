# Un autor decidió escribir un libro con varias tramas que se puede leer de forma no lineal. Es decir, por ejemplo, después del capítulo 1 puede leer el 2 o el 73; pero la historia no tiene sentido si se abordan estos últimos antes que el 1.

# Siendo un aficionado de la computación, el autor ahora necesita un orden para publicar su obra, y decidió modelar este problema como un grafo dirigido, en dónde los capítulos son los vértices y sus dependencias las aristas. Así existen, por ejemplo, las aristas (v1, v2) y (v1, v73).

# Escribir un algoritmo que devuelva un orden en el que se puede leer la historia sin obviar ningún capítulo. Indicar la complejidad del algoritmo.
from collections import deque
def obtener_orden(grafo):
    'Devolver una lista con un posible orden válido'
    cola = deque()
    orden = []
    gradosEntrada = {}
    for v in grafo.obtener_vertices():
        gradosEntrada[v] = 0
    visitados = set()
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            gradosEntrada[w] += 1
    for v in gradosEntrada:
        if gradosEntrada[v] == 0:
            cola.append(v)
    while cola:
        act = cola.popleft()
        orden.append(act)
        for w in grafo.adyacentes(act):
            gradosEntrada[w] -= 1
            if gradosEntrada[w] == 0:
                cola.append(w)
    return orden