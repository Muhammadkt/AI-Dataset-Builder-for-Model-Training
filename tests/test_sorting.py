import unittest
from curated_code.python.sorting import quicksort

class TestSorting(unittest.TestCase):
    def test_sorting(self):
        self.assertEqual(quicksort([3, 1, 4, 1, 5, 9]), [1, 1, 3, 4, 5, 9])
        self.assertEqual(quicksort([]), [])
        self.assertEqual(quicksort([5]), [5])

if __name__ == "__main__":
    unittest.main()
