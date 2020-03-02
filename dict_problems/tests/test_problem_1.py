import unittest
from problem_1 import depth_print

list_item = [i for i in range(10)]
set_item = {i for i in range(10)}
tuple_item = (i for i in range(10))
str_item = "test string"

all_items = (list_item, set_item, tuple_item, str_item)
dict_item = {i: f"data{i}" if i % 2 == 0 else {"test": i} for i in range(20)}

d = {
    "key1": 1,  # 1
    "key2": 2,  # 1
    "key3": {  # 1
        "key4": 4,  # 2
        "key5": {  # 2
            "key6": 6,  # 3
            "key7": 7,  # 3
            "key8": {  # 3
                "key9": 9,  # 4
                "key10": {  # 4
                    "key11": 10  # 5
                },
                "key12": 12     # 4
            },
            "key13": 13     # 3
        },
        "key14": {      # 2
            "key15": 15     # 3
        }
    }
}


class TestProblem1(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_depth_print(self):
        for item in all_items:
            with self.assertRaises(TypeError):
                depth_print(item)

        self.assertEqual(None, depth_print(dict_item))
        self.assertEqual(None, depth_print(d))


if __name__ == '__main__':
    unittest.main()
