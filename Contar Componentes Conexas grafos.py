# Implementar un algoritmo que reciba un grafo no dirigido y determine la cantidad mínima de aristas que debería agregársele para que el grafo sea conexo. Obviamente, si el grafo ya es conexo el algoritmo debe devolver 0. Indicar y justificar la complejidad del algoritmo implementado.

#para este ej hace falta solo contar la cantidad de componentes conexas que tiene el grafo y a esta restartle 1, por ejemplo si el grafo tiene 3 componentes conexas, solo me hacen falta 2 aristas para unir todo y que sea todo una componente conexa -> grafo conexo

def cantAristas(grafo):
  if len(grafo.obtener_vertices()) == 0:
    return 0
  visitados = set()
  cantCompConex = 0
  for v in grafo.obtener_vertices():
    if v not in visitados:
      dfs(grafo, v, visitados)
      cantCompConex+=1
  return cantCompConex - 1

def dfs(grafo, v, visitados):
  visitados.add(v)
  for w in grafo.adyacentes(v):
    if w not in visitados:
      dfs(grafo,w, visitados)
