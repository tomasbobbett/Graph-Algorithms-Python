# Implementar un algoritmo que reciba un grafo dirigido y acíclico y determine si dicho grafo admite un único orden
# topológico. Indicar y justificar la complejidad de la función. Pista: pensar qué condición puede darse para que exista
# más de un posible orden topológico.

# -Grafo dirigido
# -Aciclico 
# ¿Admite un UNICO orden topologico?
#  Pista: pensar qué condición puede darse para que exista más de un posible orden topológico.
from collections import deque
def masDeUnOrden(grafo):
  
  cola = deque()
  orden = []
  grado = {}
  for v in grafo.obtener_vertices():
    grado[v] = 0

  for v in grafo.obtener_vertices():
    for w in grafo.adyacentes(v):
      grado[w] += 1

  for v in grafo.obtener_vertices():
    if grado[v] == 0:
      cola.append(v)
    if len(cola) > 1:
      return True # ya sabemos que podemos empezar desde dos vertices distintos por lo que hay mas de un camino 
  while cola:
    if len(cola) > 1:
      return True
    act = cola.popleft()
    orden.append(act)

    for w in grafo.adyacentes(act):
      grado[w] -= 1
      if grado[w] == 0:
        cant +=1
        cola.append(w)
# hay mas de un orden cuando a la misma vez hay mas de un hijo con grado 0 que debe entrar en la cola
