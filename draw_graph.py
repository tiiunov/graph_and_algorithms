import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph, data=None):
    g = nx.Graph()
    weight, path = data
    for n1_index, n2_index, w in graph.get_all_connections():
        g.add_edge(graph.nodes[n1_index].data,
                   graph.nodes[n2_index].data,
                   weight=w)
    pos = nx.circular_layout(g)

    edge_labels = {(u, v): d['weight'] for u, v, d in g.edges(data=True)}
    nx.draw_networkx_nodes(g, pos, node_size=400,
                           node_color=['g' if n in path else 'b'
                                       for n in g.nodes()])
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels,
                                 font_color='r')
    plt.title(f'Найденный путь {path}. Вес (для BFS кол-во вершин): {weight}')
    plt.axis('off')
    plt.show()
