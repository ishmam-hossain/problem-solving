import unittest
from problem_2 import depth_print


class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)
person_c = Person("User", "2", person_b)

d = {
    "key1": 1,
    "key2": {
        "key3": 3,
        "key4": {
            "key5": 5,
            "user": person_c
        }
    },
    "key_last": "last"
}


class TestProblem2(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_depth_print(self):
        self.assertEqual(None, depth_print("ksfjkdffjfljfl"))
        self.assertEqual(None, depth_print(["ksfjkdffjfljfl", 134]))
        self.assertEqual(None, depth_print({"A": 1, "b": 2}))
        self.assertEqual(None, depth_print(("ksfjkdffjfljfl", "dff")))
        self.assertEqual(None, depth_print(d))

        with self.assertRaises(TypeError):
            depth_print(None)


if __name__ == '__main__':
    unittest.main()
