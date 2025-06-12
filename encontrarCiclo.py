def encontrar_ciclo(g):
    '''
    Devuelve una lista de vertices que conforman el ciclo. En el segundo ejemplo, 
    debería devolver [A, B, C] (o [B, C, A], etc...). 
    Si no hay ciclo, debe devolver None. 
    '''
    visitados = set()
    padre = {}
    for v in g.obtener_vertices():
        if v not in visitados:
            padre[v] = None
            ciclo = dfs(g, v, visitados, padre)
            if ciclo != None:
                return ciclo
    return None

def dfs(g, v, visitados, padre):
    visitados.add(v)
    for w in g.adyacentes(v):
        if w not in visitados:
            padre[w] = v
            resultado = dfs(g,w , visitados, padre)
            if resultado:
                return resultado
            
        elif w != padre[v]:
            #Encontramos ciclo
            inicio = w
            final = v
            act = v
            ciclo = []
            while act != inicio:
                ciclo.append(act)
                act = padre[act]
            ciclo.append(inicio)
            ciclo.reverse()
            return ciclo
    return None
