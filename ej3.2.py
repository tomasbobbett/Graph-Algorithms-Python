# Realizar el seguimiento del Algoritmo de Tarjan para obtener las componentes fuertemente conexas del siguiente grafo dirigido.
# Los pesos están únicamente para ejemplificar en el ejercicio 1.

#----------Algoritmo de Tarjan (Componentes Fuertemente Conexas) CFC

# - Tres estructuras auxiliares:
      # -orden = []
      # -masBajo = []

      # -pilaAux = Crear_pila()

# -Empezamos de un vertice aleatorio e inicializamos las estructuras en este en 0
      # -orden[origen] = 0
      # -masBajo[origen] = 0
def cfc(grafo,v, visitados, pila, apilados, orden, masBajo, cfcs, *indice):

  visitados.add(v)
  pila.apilar(v)# Pila para reconstruir el cfc
  apilados.add(v)# Pila para ver si el vertice adyacente q estoy por ver ya pertenece a una cfc
  masBajo[v] = orden[v] #Al principio esto es asi, luego cuando lo visito ya le voy a haber el orden
  for w in grafo.adyacentes(v):
    if w not in vistiados:
      orden[w] = *(indice) + 1 
      *indice+=1
      cfc(grafo,w,visitados,pila,apilados,orden,masBajo, cfcs)
      masBajo[v] = min(masBajo[w], masBajo[v]) #Si su hijo tiene un MB mas chico, este se actualiza
    elif w in apilados:
      masBajo[v] =  min(masBajo[v], orden[w])#si encuentra un vertice adyacente con un ORDEN mas pequeño se actualiza mambien
  if masBajo[v] == orden[v]: #LUEGO de recorrer todos sus adyacentes, si el mb = orden entonces se cierra un cfc, sino no 
    nueva_cfc = []
    do: 
      w = pila.Desapilar()
      apilados.remove(w) #apilar hasta llegar al nodo que tenia orden = mb
      nueva_cfc.append(w)
    while w not v
    cfcs.append(nueva_cfc) #apendear a la lista de listas
