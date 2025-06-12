# Implementar el algoritmo para arobol de tendido minimo el 


# ---------------Alogritmo de Kruskal--------------

def kruskal(grafo):
  #O(V)
  conjuntos = UnionFind(grafo.obtener_vertices()) #Tipo de dato abstracto que no conocemos
  # o(e log(v))
  aristas = sort(obtener_aristas(grafo))#Arreglo de aristas ordenadas trupla ( a, b, pesoAristaA-B )
  # O(v)
  arbol = Grafo(False, grafo.obtener_vertices())
  #o(e)
  for a in aristas:
    v, w, peso = a
    # o(1)
    if conjuntos.find(v) == conjuntos.find(w): #Si conjuntos detecta que v y w pertenecen al mismo conjunto continua
      continue
    # O(1)
    arbol.agregar_arista(v,w, peso)#si no lo hace se agrega al arbol de tendido 
    conjuntos.union(v,w)# Y los une en el conjunto UnionFind para no repetirlo
  return arbol

  # La complejidad del algoritmo es de O(e log(e))