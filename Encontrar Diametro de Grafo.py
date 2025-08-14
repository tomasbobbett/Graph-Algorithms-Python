from collections import deque
def diametro(grafo):
    if len(grafo.obtener_vertices())==0:
        return 0 #Si el grafo es nulo, el diametro sera 0
          

    maximoA = 0
    maximoB=0
    origen = grafo.vertice_aleatorio()
    a,maximoA = bfs(grafo,origen)
    b,maximoB = bfs(grafo,a)      # La clave es buscar un vertice aleatorio y su vertuice mas alejado, el diametro sera la distancia mas grande entre la distancia maxima al otro vertice del primer aleatorio con la distancia del vertice que encontramos mas alejado del primer aleatrio :)
    if maximoA > maximoB:
        return maximoA
    return maximoB

def bfs(grafo, origen):
    distancias = {}
    for v in grafo.obtener_vertices():
        distancias[v] = 0
    cola = deque()
    cola.append(origen)
    visitados = set()
    visitados.add(origen)
    while cola:
        act = cola.popleft()
        for w in grafo.adyacentes(act):
            if w not in visitados:
                visitados.add(w)
                distancias[w]=distancias[act]+1
                cola.append(w)
    maxima = 0
    vMax = origen
    for v in grafo.obtener_vertices():
        if distancias[v] > maxima:
            maxima = distancias[v]
            vMax = v
    return v,maxima