# função para busca em largura (BFS)
def busca_em_largura(grafo, inicio):
    if grafo == {}:
        print("grafo vazio.")
        return
    if inicio not in grafo:
        print("vertice inicial nao existe no grafo.")
        return
    else:
        visitados = []        
        fila = [inicio]       

        while fila:     
            vertice = fila.pop(0) #retira  o primeiro vertice da fila e add em vertice

            if vertice not in visitados:
                visitados.append(vertice)   # marca como visitado

                # adiciona todos os vizinhos à fila
                for vizinho in grafo[vertice]:
                    if vizinho not in visitados: #verifica se vizinho ja foi percorrido
                        if vizinho not in fila:
                            fila.append(vizinho) 

        return visitados

def menor_caminho(grafo, inicio, fim):
    visitados = []
    # a fila vai ser um dicionario
    fila = {
            'vertice': inicio,
            'caminho': [inicio]
        }
    while fila:
        visitado = fila['caminho'].pop(0)
        if visitado == fim:
            return fila['caminho']
        visitados.append(visitado)
        for vizinho in grafo[visitado]:
            if vizinho not in fila['caminho']:
                if vizinho not in visitados:
                    novo_caminho = list(fila['caminho'])
                    novo_caminho.append(vizinho)
                    fila = {
                        'vertice': vizinho,
                        'caminho': novo_caminho
                    }
    return

#cria um dicionario vazio que será nosso grafo
def criar_grafo():
    return {} 

#adiciona vertice ao grafo (sem aresta)
def add_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = [] #adiciona o vertice com uma lista vazia de adjacentes
    else:
        print("vertice ja existe no grafo.")
    return grafo

#cria aresta entre vertices que existem no grafo
def add_aresta(grafo, origem, destino, naoDirecionado = False):
    if origem in grafo and destino in grafo:
        grafo[origem].append(destino) #adiciona a aresta entre os vertices
        if naoDirecionado:
            grafo[destino].append(origem) #adiciona a aresta no sentido contrario se for nao direcionado
    else:
        print("um dos vertices nao existe no grafo.")
    return grafo
            
#cria grafo pronto para teste 
def nao_direcionado_pronto():
    grafo = criar_grafo()
    add_vertice(grafo, 'A')
    add_vertice(grafo, 'B')
    add_vertice(grafo, 'C')
    add_vertice(grafo, 'D')
    add_vertice(grafo, 'E')
    # 3. Adiciona todas as arestas
    add_aresta(grafo, 'A', 'B', naoDirecionado=True)
    add_aresta(grafo, 'A', 'C', naoDirecionado=True)
    add_aresta(grafo, 'B', 'C', naoDirecionado=True)
    add_aresta(grafo, 'C', 'D', naoDirecionado=True)
    add_aresta(grafo, 'D', 'E', naoDirecionado=True)
    return grafo


def main():

    grafo = nao_direcionado_pronto()
    print("=" * 50)
    print("exibir grafo \n:", grafo)
    print("=" * 50)

    listaVisitados = busca_em_largura(grafo, 'A')
    print("Lista de visitados: \n", listaVisitados)
    print("=" * 50)
        

if __name__ == "__main__":
    main()
