# Realizar un seguimiento de aplicar el algoritmo de Prim (desde el vértice A)
#  para obtener el árbol de tendido mínimo del siguiente grafo.

def prim(grafo):
  vertice = grafo.vertice_aleatorio() #Comienzo en un vertice aleatorio
  visitados = set()
  visitados.agregar(vertice) #Ya visito el origen de primeras
  q = heap_crear()  #Necesito el heap ordenando por peso de aristas
  arbol = Grafo(False, grafo.obtener_vertices()) #Creo el futuro arbol de tendido

  for w in grafo.adyacentes(vertice):
    q.Encolar((vertice,w), grafo.peso_arista(vertice,w)) #Encolo todas las aristas con su peso 

  while not q.EstaVacia(): #Voy a estar procesando mientras el heap tenga alguna arista

    (vertice,w) = q.Desencolar() #Desencolo la arista MENOS pesada

    if w in visitados:
      continue #Si ya visite ese vertice paso y sigo con el proximo en el heap

    arbol.agregar_arista(vertice, w, grafo.peso_arista(vertice,w)) #Como no lo visite aun, agrego al 
    # arbol de tendido desde el padre del q estaba revisando los adyacentes (vertice o v)

    visitados.add(w) #Agrego como visitado el que agregue al arbol de tendido (w)
    
    for u in grafo.adyacentes(w):#Veo los adyacentes del vertice q acabamos de agregar al arbol 
      # Adyacentes de (w) => (u)
      if u not in visitados:
        q.encolar((w,u), grafo.peso_arista(w, u)) #Si no estan visitados ir agregando al heap
  return arbol
