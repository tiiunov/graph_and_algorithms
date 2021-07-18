from algorithms.base_algorithm import BaseAlgorithm


class FordBellman(BaseAlgorithm):
    def __init__(self, name):
        super().__init__(name)

    def find_path(self, graph, start, end):
        return self.ford_bellman(graph, start, end)

    @staticmethod
    def ford_bellman(graph, start, end):
        count = len(graph.nodes)
        all_connections = graph.get_all_connections()
        dist = [float("Inf")] * count
        dist[start.index] = 0
        paths = []
        for i in range(count):
            paths.append([graph.nodes[end.index].data])
        for i in range(count - 1):
            for u, v, w in all_connections:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    paths[v].append(graph.nodes[u].data)
        paths[end.index].append(graph.nodes[start.index].data)
        for u, v, w in all_connections:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        paths[end.index].reverse()
        return dist[end.index], paths[end.index]
