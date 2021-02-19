import unittest

from attrdict import AttrMap

from src.dinics_solver import DinicsAlgorithm
from src.graph import Graph


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case_01 = AttrMap({
            "sources": [0],
            "sinks": [3],
            "paths": [
                [0, 7, 0, 0],
                [0, 0, 6, 0],
                [0, 0, 0, 8],
                [9, 0, 0, 0]
            ],
            "solution": 6,
        }, sequence_type=list)

        self.test_case_02 = AttrMap({
            "sources": [0, 1],
            "sinks": [4, 5],
            "paths": [
                [0, 0, 4, 6, 0, 0],
                [0, 0, 5, 2, 0, 0],
                [0, 0, 0, 0, 4, 4],
                [0, 0, 0, 0, 6, 6],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ],
            "solution": 16,
        }, sequence_type=list)

    @staticmethod
    def solution(entrances, exits, path):
        graph = Graph().construct(path, entrances, exits)
        graph.get_max_flow(DinicsAlgorithm)

        return graph.max_flow

    def test_solution_01(self):
        solution = self.solution(
            self.test_case_01.sources,
            self.test_case_01.sinks,
            self.test_case_01.paths
        )
        self.assertEqual(self.test_case_01.solution, solution)

    def test_solution_02(self):
        solution = self.solution(
            self.test_case_02.sources,
            self.test_case_02.sinks,
            self.test_case_02.paths
        )
        self.assertEqual(self.test_case_02.solution, solution)


if __name__ == '__main__':
    unittest.main()
