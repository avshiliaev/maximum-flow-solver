from src.abstractions import AbstractGraph, AbstractSolver

INF = float("inf")


class Graph(AbstractGraph):
    def __init__(self):

        super().__init__()
        self.flow_graph = None
        self.source = None
        self.sink = None

        self.max_flow = None

    def construct(self, _flow_graph, _sources_list, _sinks_list):
        """
        Factory method to construct an instance of a graph.

        Args:
            _flow_graph (List[List[int]]): Flow graph as an adjacency matrix.
            _sources_list (List[int]): List of source nodes.
            _sinks_list (List[int]): List of sink nodes.

        Returns:
            self: Factory method to construct an instance of a graph.
        """
        self.flow_graph = _flow_graph

        _nodes_number = len(_flow_graph)

        self.source = _nodes_number
        self.sink = _nodes_number + 1

        for row in range(_nodes_number):
            self.flow_graph[row].append(0)
            self.flow_graph[row].append(INF if row in _sinks_list else 0)

        _nodes_number += 2

        self.flow_graph.append([(INF if x in _sources_list else 0) for x in range(_nodes_number)])
        self.flow_graph.append([0] * _nodes_number)

        return self

    def get_max_flow(self, algorithm: AbstractSolver):
        """
        Solve the maximum flow problem on the graph.

        Args:
            algorithm: Maximum flow algorithm.

        Returns:
            int: Maximum flow.
        """
        if self.flow_graph and self.source and self.sink:
            solver = algorithm(self)
            self.max_flow = solver.solve()
