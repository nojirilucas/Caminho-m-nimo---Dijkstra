import networkx as nx
import matplotlib.pyplot as plt

def ler_grafo_do_arquivo(nome_arquivo):
    G = nx.DiGraph()
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            origem, destino, peso = map(int, linha.split())
            G.add_edge(origem, destino, weight=peso)
    return G

def visualizar_grafo(G, menor_caminho=None):
    pos = nx.circular_layout(G)  # Define as posições dos nós em um círculo
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold', arrowsize=20)

    # Desenha todas as arestas em preto
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')

    # Se um caminho mínimo foi fornecido, desenha esse caminho em verde
    if menor_caminho:
        edges_in_path = [(menor_caminho[i], menor_caminho[i+1]) for i in range(len(menor_caminho)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='green', width=3)

    labels_arestas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_arestas, font_color='red')
    plt.title('Grafo Direcionado com Pesos')
    plt.show()

def principal():
    nome_arquivo = "text"

    # Solicita os vértices de origem e destino ao usuário
    vertice_origem = int(input("Digite o vértice de origem: "))
    vertice_destino = int(input("Digite o vértice de destino: "))

    G = ler_grafo_do_arquivo(nome_arquivo)
    menor_caminho = nx.shortest_path(G, source=vertice_origem, target=vertice_destino, weight='weight')
    visualizar_grafo(G, menor_caminho)

    distancia_minima = nx.shortest_path_length(G, source=vertice_origem, target=vertice_destino, weight='weight')

    print(f"Distância mínima de {vertice_origem} para {vertice_destino}: {distancia_minima}")
    print(f"Caminho mínimo de {vertice_origem} para {vertice_destino}: {' -> '.join(map(str, menor_caminho))}")

if __name__ == "__main__":
    principal()
