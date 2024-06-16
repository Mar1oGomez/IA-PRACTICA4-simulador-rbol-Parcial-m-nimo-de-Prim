#Mario Alberto Gomez Temores      21310159     15\06\24
import heapq
import matplotlib.pyplot as plt
import networkx as nx

def prim(graph, start_node):
    # Inicializacion de variables
    minimum_spanning_tree = []
    visited = {node: False for node in graph}
    min_heap = [(0, start_node)]  # (peso, nodo)
    total_cost = 0
    
    while min_heap:
        # Extraer el nodo con el menor peso del heap
        weight, node = heapq.heappop(min_heap)
        
        if visited[node]:
            continue
        
        # Marcar el nodo como visitado
        visited[node] = True
        total_cost += weight
        
        if node != start_node:
            minimum_spanning_tree.append((node, weight))
        
        # Anadir vecinos no visitados al heap
        for neighbor, weight in graph[node].items():
            if not visited[neighbor]:
                heapq.heappush(min_heap, (weight, neighbor))
        
        # Mostrar el estado actual del grafo
        print(f"Visited: {visited}")
        print(f"Minimum Spanning Tree: {minimum_spanning_tree}")
        print(f"Total Cost: {total_cost}\n")
        
        # Dibujar el grafo actualizado
        draw_graph(graph, minimum_spanning_tree, visited, total_cost)

def draw_graph(graph, mst_edges, visited, total_cost):
    # Crear un objeto Graph de networkx
    G = nx.Graph()
    
    # Anadir nodos y aristas al grafo
    for node in graph:
        G.add_node(node)
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)
    
    # Calcular las posiciones de los nodos para la visualizacion
    pos = nx.spring_layout(G)
    
    # Dibujar nodos y aristas base del grafo
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold')
    
    # Dibujar aristas del MST en color verde
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='g', width=2.0)
    
    # Marcar nodos visitados en color rojo
    nx.draw_networkx_nodes(G, pos, nodelist=[node for node, vis in visited.items() if vis], node_color='r', node_size=1500)
    
    # Mostrar etiquetas con informacion adicional
    labels = {node: f"{node}" for node in graph}
    nx.draw_networkx_labels(G, pos, labels, font_size=12)
    
    # Configurar titulo del grafico
    plt.title(f'Minimum Spanning Tree (Total Cost: {total_cost})')
    
    # Mostrar el grafico actualizado
    plt.show()

# Ejemplo de uso
graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'D': 1, 'C': 1},
    'C': {'B': 1, 'D': 1, 'E': 4},
    'D': {'A': 3, 'B': 1, 'C': 1, 'E': 5},
    'E': {'C': 4, 'D': 5}
}

start_node = 'A'
prim(graph, start_node)

