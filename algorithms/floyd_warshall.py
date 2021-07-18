import numpy as np
from copy import deepcopy
from algorithms.base_algorithm import BaseAlgorithm


class FloydWarshall(BaseAlgorithm):
    def __init__(self, name):
        super().__init__(name)

    def find_path(self, graph, start, end):
        return self.floyd_warshall(graph, start, end)

    def floyd_warshall(self, graph, start, end):
        n_graph = deepcopy(graph.adj_matrix)
        v = len(n_graph)
        p = np.zeros((v, v))
        for i in range(0, v):
            for j in range(0, v):
                p[i, j] = i
                if i != j and n_graph[i][j] == 0:
                    p[i, j] = float("-inf")
                    n_graph[i][j] = float("+inf")

        for k in range(0, v):
            for i in range(0, v):
                for j in range(0, v):
                    if n_graph[i][j] > n_graph[i][k] + n_graph[k][j]:
                        n_graph[i][j] = n_graph[i][k] + n_graph[k][j]
                        p[i, j] = p[k, j]
        index_result = []
        self.combine_path(p, start.index, end.index, index_result)
        result = []
        for i in index_result:
            result.append(graph.nodes[i].data)
        return n_graph[start.index][end.index], result

    def combine_path(self, p, i, j, ind_res):
        i, j = int(i), int(j)
        if i == j:
            ind_res.append(i)
        elif p[i, j] == float("-inf"):
            print('path does not exist')
        else:
            self.combine_path(p, i, p[i, j], ind_res)
            ind_res.append(j)
