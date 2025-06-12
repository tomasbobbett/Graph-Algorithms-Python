from collections import deque
def a_n_aristas(grafo, v, n):
    if n == 0:
        return [v]
    
    distancias = {}
    visitados = set()
    cola = deque()
    res = []

    origen = v

    cola.append(origen)
    distancias[origen] =0 
    visitados.add(origen)

    while cola:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                distancias[w] = distancias[v] +1 
                if distancias[w] == n:
                    res.append(w)
                cola.append(w)
                visitados.add(w)
    return res