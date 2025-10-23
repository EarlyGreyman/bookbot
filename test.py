import unittest
from stats import sort_dict


class TestSortDict(unittest.TestCase):
    def test_sort_dict_basic(self):
        """Test that sort_dict sorts by frequency in descending order"""
        input_dict = {"a": 5, "b": 2, "c": 8, "d": 1}
        expected = [
            {"char": "c", "num": 8},
            {"char": "a", "num": 5},
            {"char": "b", "num": 2},
            {"char": "d", "num": 1}
        ]
        result = sort_dict(input_dict)
        self.assertEqual(result, expected)

    def test_sort_dict_empty(self):
        """Test that sort_dict handles empty dictionary"""
        input_dict = {}
        expected = []
        result = sort_dict(input_dict)
        self.assertEqual(result, expected)

    def test_sort_dict_single_item(self):
        """Test that sort_dict handles single item dictionary"""
        input_dict = {"x": 10}
        expected = [{"char": "x", "num": 10}]
        result = sort_dict(input_dict)
        self.assertEqual(result, expected)

    def test_sort_dict_equal_values(self):
        """Test that sort_dict handles equal frequency values"""
        input_dict = {"a": 3, "b": 3, "c": 3}
        result = sort_dict(input_dict)
        # All items should have num=3
        for item in result:
            self.assertEqual(item["num"], 3)
        # Should have 3 items
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()
