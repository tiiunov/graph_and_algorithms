from collections import deque
from algorithms.base_algorithm import BaseAlgorithm


class Bfs(BaseAlgorithm):
    def __init__(self, name):
        super().__init__(name)

    def find_path(self, graph, start, end):
        return self.bfs(graph, start, end)

    @staticmethod
    def bfs(graph, start, end):
        track = {start.index: float("Inf")}
        queue = deque()
        queue.append(start.index)
        while len(queue) != 0:
            nod_ind = queue.popleft()
            for n, d in graph.connections_from(graph.nodes[nod_ind]):
                if n.index in track.keys():
                    continue
                track[n.index] = nod_ind
                queue.append(n.index)
            if end.index in track.keys():
                break
        path_item = end.index
        ind_result = []
        while path_item != float("Inf"):
            ind_result.append(path_item)
            path_item = track[path_item]
        ind_result.reverse()
        result = []
        for i in ind_result:
            result.append(graph.nodes[i].data)
        return len(result), result
