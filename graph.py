class Graph:
    def __init__(self, nodes_count, nodes=None):
        self.adj_matrix = [[0] * nodes_count for _ in range(nodes_count)]
        self.nodes = nodes
        for index, node in enumerate(self.nodes):
            node.index = index

    @classmethod
    def create_graph(cls, nodes):
        return Graph(len(nodes), nodes)

    def connect_directionally(self, node_from, node_to, weight=1):
        self.adj_matrix[node_from.index][node_to.index] = weight

    def connect(self, node1, node2, weight=1):
        self.connect_directionally(node1, node2, weight)
        self.connect_directionally(node2, node1, weight)

    def connections_from(self, node):
        result = []
        for i, n in enumerate(self.nodes):
            if self.adj_matrix[node.index][i] != 0:
                result.append((n, self.adj_matrix[node.index][i]))
        return result

    def connections_to(self, node):
        result = []
        column = [row[node.index] for row in self.adj_matrix]
        for i, n in enumerate(self.nodes):
            if column[i] != 0:
                result.append((n, column[i]))
        return result

    def get_all_connections(self):
        result = []
        for node in self.nodes:
            arr = self.connections_from(node)
            for n, d in arr:
                result.append([node.index, n.index, d])
        return result
