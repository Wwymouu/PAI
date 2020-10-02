import unittest
import core

class TestDSeparation1(unittest.TestCase):

    # +---+     +---+     +---+     +---+     +---+
    # | X |---->| Y |---->| Z |<----| V |<----| W |
    # +---+     +---+     +---+     +---+     +---+

    def setUp(self) -> None:
        g = core.BayesNet()
        g.add_nodes_from(['X', 'Y', 'Z', 'V', 'W'])
        g.add_edges_from([('X', 'Y'), ('Y', 'Z'), ('V', 'Z'), ('W', 'V')])
        self.g = g

    def test_a(self):
        reachable = self.g.get_reachable('X', plot=False)
        assert reachable == {'Y', 'Z'}

    def test_b(self):
        reachable = self.g.get_reachable('X', ['Z'], plot=False)
        assert reachable == {'Y', 'V', 'W'}

    def test_c(self):
        reachable = self.g.get_reachable('Z', [], plot=False)
        assert reachable == {'X', 'Y', 'V', 'W'}

    def test_d(self):
        reachable = self.g.get_reachable('Z', ['Z'], plot=False)
        assert len(reachable) == 0

class TestDSeparation2(unittest.TestCase):

    #                               +---+
    #                              -| W |
    # +---+     +---+     +---+  -- +---+
    # | V |---->| Z |<----| Y |<-
    # +---+     +---+     +---+  -- +---+
    #                              -| X |
    #                               +---+

    def setUp(self) -> None:
        g = core.BayesNet()
        g.add_nodes_from(['X', 'Y', 'Z', 'V', 'W'])
        g.add_edges_from([('V', 'Z'), ('Y', 'Z'), ('X', 'Y'), ('W', 'Y')])
        self.g = g

    def test_a(self):
        reachable = self.g.get_reachable('W', plot=False)
        assert reachable == {'Y', 'Z'}

    def test_b(self):
        reachable = self.g.get_reachable('W', ['Y'], plot=False)
        assert reachable == {'X'}

if __name__ == '__main__':
    unittest.main()