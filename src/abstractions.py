from abc import ABC, abstractmethod


class AbstractSolver(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def solve(self):
        ...


class AbstractGraph(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def construct(self, _flow_graph, _sources_list, _sinks_list):
        ...

    @abstractmethod
    def get_max_flow(self, algorithm: AbstractSolver):
        ...
