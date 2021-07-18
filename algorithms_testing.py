from graph import Graph
from node import Node
from timer import time_of_function
from memory import mem_of_function
from memory_profiler import profile
from algorithms.floyd_warshall import FloydWarshall
from algorithms.dijkstra import Dijkstra
from algorithms.astar import Astar
from algorithms.ford_bellman import FordBellman
from algorithms.bfs import Bfs
from draw_graph import draw_graph


@time_of_function
def dijkstra_time_test(graph, start, end):
    algorithm = Dijkstra('Dijkstra')
    for _ in range(50000):
        algorithm.find_path(graph, start, end)
    print(algorithm.find_path(graph, start, end))


@time_of_function
def floyd_time_test(graph, start, end):
    algorithm = FloydWarshall('Floyd-Warshall')
    for _ in range(50000):
        algorithm.find_path(graph, start, end)
    print(algorithm.find_path(graph, start, end))


@time_of_function
def ford_bellman_time_test(graph, start, end):
    algorithm = FordBellman('Ford-Bellman')
    for _ in range(50000):
        algorithm.find_path(graph, start, end)
    print(algorithm.find_path(graph, start, end))


@time_of_function
def bfs_time_test(graph, start, end):
    algorithm = Bfs('BFS')
    for _ in range(50000):
        algorithm.find_path(graph, start, end)
    print(algorithm.find_path(graph, start, end))


@time_of_function
def a_star_time_test(graph, start, end):
    algorithm = Astar('A_star')
    for _ in range(50000):
        algorithm.find_path(graph, start, end)
    print(algorithm.find_path(graph, start, end))


@mem_of_function
def dijkstra_memory_test(graph, start, end):
    algorithm = Dijkstra('Dijkstra')
    for _ in range(50000):
        algorithm.find_path(graph, start, end)


@mem_of_function
def floyd_memory_test(graph, start, end):
    algorithm = FloydWarshall('Floyd-Warshall')
    for _ in range(50000):
        algorithm.find_path(graph, start, end)


@mem_of_function
def ford_memory_test(graph, start, end):
    algorithm = FordBellman('Ford-Bellman')
    for _ in range(50000):
        algorithm.find_path(graph, start, end)


@profile
def bfs_memory_test(graph, start, end):
    algorithm = Bfs('BFS')
    for _ in range(50000):
        algorithm.find_path(graph, start, end)


@mem_of_function
def a_star_memory_test(graph, start, end):
    algorithm = Astar('A_star')
    for _ in range(50000):
        algorithm.find_path(graph, start, end)


if __name__ == "__main__":
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")

    w_graph = Graph.create_graph([a, b, c, d, e, f])

    w_graph.connect(a, b, 5)
    w_graph.connect(a, c, 10)
    w_graph.connect(a, e, 2)
    w_graph.connect(b, c, 2)
    w_graph.connect(b, d, 4)
    w_graph.connect(c, d, 7)
    w_graph.connect(c, f, 10)
    w_graph.connect(d, e, 3)

    dijkstra_memory_test(w_graph, b, f)
    dijkstra_time_test(w_graph, b, f)
    a_star_time_test(w_graph, b, f)
    floyd_time_test(w_graph, b, f)
    ford_bellman_time_test(w_graph, b, f)
    bfs_time_test(w_graph, b, f)
    alg = Dijkstra('Dijkstra')
    draw_graph(w_graph, alg.find_path(w_graph, b, f))
