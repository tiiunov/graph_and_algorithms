from algorithms.base_algorithm import BaseAlgorithm


class Dijkstra(BaseAlgorithm):
    def __init__(self, name):
        super().__init__(name)

    def find_path(self, graph, start, end):
        return self.dijkstra(graph, start, end)

    @staticmethod
    def dijkstra(graph, start, end):
        finish_index = start.index

        dist = [None] * len(graph.nodes)
        for i, n in enumerate(dist):
            dist[i] = [float("+inf")]
            dist[i].append([graph.nodes[finish_index]])

        dist[finish_index][0] = 0

        queue = [i for i, n in enumerate(graph.nodes)]
        seen = set()
        while len(queue) > 0:
            min_dist = float("+inf")
            min_node = 0
            for n in queue:
                if dist[n][0] < min_dist and n not in seen:
                    min_dist = dist[n][0]
                    min_node = n
            try:
                queue.remove(min_node)
            except ValueError:
                print('path does not exist')
            seen.add(min_node)

            if min_node == end.index:
                final_weight = dist[end.index][0]
                path = [nod.data for nod in dist[end.index][1]]
                return final_weight, path

            connections = graph.connections_from(graph.nodes[min_node])
            for (start, weight) in connections:
                tot_dist = weight + min_dist
                if tot_dist < dist[start.index][0]:
                    dist[start.index][0] = tot_dist
                    dist[start.index][1] = list(dist[min_node][1])
                    dist[start.index][1].append(start)
