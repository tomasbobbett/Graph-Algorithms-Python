# Implementar un algoritmo que, dado un grafo pesado (con pesos positivos), un vértice v y otro w, determine el camino mínimo
# de v a w dentro del grafo, con una modificación: en caso de encontrar más de un camino mínimo, que desempate por aquel de
# menor cantidad de aristas. Considerar que, justamente, podrían haber varios caminos de una misma distancia, que a su vez
# sean la mínima. Indicar y justificar la complejidad del algoritmo implementado.
# Por ejemplo, en el grafo de arriba hay 2 caminos mínimos del vértice A al vértice D: A -> D, A -> E -> D, ambos de costo 3,
# por lo que se debe elegir el primero por ser de menor cantidad de aristas.

def caminoMinimo(grafo, origen, destino):
  visitados = set()
  padre = {}
  cantAristas = {}
  caminosMinimos = []
  padre[origen] = None
  distancia = {}
  h = heap_crear()
  
  for v in grafo.obtener_vertices():
    cantAristas[v] = 'inf'
    distancia[v] = 'inf'
  distancia[origen] = 0
  cantAristas[origen] = 0
  h.encolar(origen, distancia[origen])

  while not h.esta_vacia():
    vertAct, distAct = h.desencolar()

    if distAct > distancia[vertAct]:
      continue

    for w in grafo.adyacentes(vertAct):
      if distancia[w] > distancia[vertAct] + grafo.peso(vertAct, w):
        cantAristas[w] = cantAristas[vertAct] + 1
        distancia[w] = distancia[vertAct] + grafo.peso(vertAct, w)
        padre[w] = vertAct
        h.encolar(w, distancia[w])

      elif  distancia[w] == distancia[vertAct] + grafo.peso(vertAct, w) and cantAristas[w] > 1 + cantAristas[vertAct]:
        cantAristas[w] = cantAristas[vertAct] + 1
        distancia[w] = distancia[vertAct] + grafo.peso(vertAct, w)
        padre[w] = vertAct
        h.encolar(w, distancia[w])

        
  if destino not in padre:
        return None  # No hay camino
  act = destino
  camino = []
  while act not origen:
    camino.append(act)
    act = padre[act]
  camino.append(origen)
  return reversed(camino)
