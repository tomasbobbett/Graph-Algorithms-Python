# Daniel debe repartir a N invitados entre DOS mesas
from collections import deque
def repartir_invitados(grafo):
  # Reconstruimos grafo complemento-------------------
  grafoCompl = Grafo(False, grafo.obtener_vertices())
  for v in grafo.obtener_vertices():
    for w in grafo.obtener_vertices():
      if not grafo.estan_unidos(v, w) and v != w:
        grafoCompl.unir(v, w)
  # Comprobamos si el grafo complemento es bipartito------------------------

  color = {}
  raiz = grafoCompl.vertice_aleatorio()
  color[raiz] = 0
  cola = deque()
  cola.append(raiz)
  visitados = set()
  while cola:
    act = cola.popleft()
    for w in grafoCompl.adyacentes(act):
      if w not in visitados:
        color[w] = 1 - color[act]
        if color[w] == color[act]:
          return KeyError("error en separar en mesas")
        cola.append(w)
        visitados.add(w)
  mesa1 = []
  mesa2 = []
  for v in grafoCompl.obtener_vertices():
    if color[v] == 1:
      mesa1.append(v)
    elif color[v] == 0:
      mesa2.append(v)
  return mesa1, mesa2
