import unittest
from problem_3 import lca


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent


root_node = Node(1)
left1 = Node(2, root_node)
left2 = Node(2, root_node)
left4 = Node(4, left2)
left5 = Node(5, left2)
left8 = Node(8, left4)
left9 = Node(9, left4)
left10 = Node(10, left9)
left11 = Node(11, left10)
left12 = Node(12, left11)
left13 = Node(13, left12)
left14 = Node(14, left13)
right3 = Node(3, root_node)
right6 = Node(6, right3)
right7 = Node(7, right3)


class TestProblem3(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_lca(self):
        with self.assertRaises(TypeError):
            lca(None, None)

        with self.assertRaises(TypeError):
            lca(right3, None)

        with self.assertRaises(TypeError):
            lca(None, left13)

        with self.assertRaises(TypeError):
            lca(Node(value=None, parent=right3), None)

        with self.assertRaises(AttributeError):
            lca(right7, Node(value=None, parent=root_node))

        with self.assertRaises(AttributeError):
            lca(Node(value=None, parent=root_node), left13)

        self.assertEqual(2, lca(left1, left1))
        self.assertEqual(4, lca(left14, left4))
        self.assertEqual(3, lca(right6, right7))
        self.assertEqual(3, lca(right3, right7))
        self.assertEqual(1, lca(root_node, left9))


if __name__ == '__main__':
    unittest.main()
