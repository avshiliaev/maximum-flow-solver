from src.abstractions import AbstractSolver


class DinicsAlgorithm(AbstractSolver):
    def __init__(self, graph):

        super().__init__()
        self.graph = graph
        self.lvl_graph = None

    # Build level_graph by using BFS
    def _bfs(self, flow_graph, _a_paths, _source, _sink):
        """
        Breadth-First-Search to construct a level graph.

        Args:
            flow_graph (List[List[int]]): Flow graph as an adjacency matrix.
            _a_paths (List[List[int]]): Augmented paths graph.
            _source (int): Source node index.
            _sink (int): Sink node index.

        Returns:
            bool: Return whether the sink node is reached while BFS.
        """
        # initialize a queue for the BFS and immediately add the source node since we always start at it
        queue = [_source]
        # mark each node as unvisited
        self.lvl_graph = len(flow_graph) * [0]
        # mark the distance to the source node to be 1
        self.lvl_graph[_source] = 1

        # iterate while queue is not empty
        while queue:
            # remove first node index we find in the queue and iterate through all the adjacent edges of that node
            k = queue.pop(0)
            for i in range(len(flow_graph)):
                # Remaining capacity is greater than zero and we take only not visited nodes
                if (_a_paths[k][i] < flow_graph[k][i]) and (self.lvl_graph[i] == 0):
                    # compute the level of the node and add it to the queue
                    self.lvl_graph[i] = self.lvl_graph[k] + 1
                    queue.append(i)
            # the process continues until the queue is empty and the entire lvl graph is built

        # return whether we were able to reach the sink node while BFS
        return self.lvl_graph[_sink] > 0

    # Search augmenting path by using DFS
    def _dfs(self, _flow_graph, _a_paths, _source, _remaining_capacity):
        """
        Depth-First-Search to find blocking flows.

        Args:
            _flow_graph (List[List[int]]): Flow graph as an adjacency matrix.
            _a_paths (List[List[int]]): Augmented paths graph.
            _source (int): Source node index.
            _remaining_capacity (int): Remaining capacity of a blocking flow.

        Returns:
            bool: Maximum flow of the graph.
        """

        # we can stop if we reach the sink node
        if _source == len(_flow_graph) - 1:
            return _remaining_capacity

        tmp = _remaining_capacity
        for i in range(len(_flow_graph)):
            # Remaining capacity is greater than zero and it goes upper level
            if (self.lvl_graph[i] == self.lvl_graph[_source] + 1) and (_a_paths[_source][i] < _flow_graph[_source][i]):
                # Proceed recursively to get the bottleneck value
                _bottleneck_value = self._dfs(
                    _flow_graph, _a_paths, i, min(tmp, _flow_graph[_source][i] - _a_paths[_source][i])
                )
                # Augment paths with the bottleneck value
                _a_paths[_source][i] = _a_paths[_source][i] + _bottleneck_value
                _a_paths[i][_source] = _a_paths[i][_source] - _bottleneck_value
                tmp = tmp - _bottleneck_value

        return _remaining_capacity - tmp

    # Calculate the maximum flow
    def solve(self):
        """
        Calls the solver.

        Returns:
            int: Maximum flow of the graph.
        """
        max_flow = 0
        augmented_paths = [len(self.graph.flow_graph) * [0] for _ in range(len(self.graph.flow_graph))]
        while self._bfs(self.graph.flow_graph, augmented_paths, self.graph.source, self.graph.sink):
            max_flow = max_flow + self._dfs(self.graph.flow_graph, augmented_paths, self.graph.source, 1)

        return max_flow
