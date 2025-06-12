# Implementar un algoritmo que, dado un grafo pesado (con pesos positivos), un vértice v y otro w, determine la cantidad de caminos mínimos que hay de v a w dentro del grafo. Considerar que, justamente, podrían haber varios caminos de una misma distancia, que a su vez sean la mínima. Indicar y justificar la complejidad del algoritmo implementado.
# Por ejemplo, en el grafo de abajo hay 3 caminos mínimos del vértice A al vértice 
#  A -> E,
#  A -> B -> F -> D -> E,
#  A -> H -> F -> D -> E,
#  todos de costo 8.

def caminosMinimos(grafo, origen, destino):
  # Debemos hacer un dijkstra completo y luego encontrar los caminos minimos hasta w

  distancia = {}
  q = heap_crear()#   -------------  INICIALIZAR ESTRUCTURAS AUXILIARES 
  cantCaminosA = {}
  caminos = []
  
  for v in grafo.obtener_vertices():
    cantCaminosA[v] = 0
    distancia[v] = 'inf'

  cantCaminosA[origen] = 1
  distancia[origen] = 0 #----------------INICIALIZAR ORIGEN EN ESTRUCTURAS
  q.append(0, origen)
  
  while not q.esta_vacia():

    distAct, vertAct = q.Desencolar()
    if distAct > distancia[vertAct]:
      continue # Saco de la cola un vertice con distancia que ya no me sirve porq ya encontre un camino mas corto asi q continuo

    for w in grafo.adyacentes(vertAct):
      if distancia[w] > distancia[vertAct] + grafo.peso(vertAct,w):
        distancia[w] = distancia[vertAct] + grafo.peso(vertAct,w)
        cantCaminosA[w] = cantCaminosA[vertAct]
        q.Encolar(distancia[w], w)
      elif distancia[w] == distancia[vertAct] + grafo.peso(vertAct, w):
        cantCaminosA[w] += cantCaminosA[vertAct]
  return cantCaminosA[destino]
  
