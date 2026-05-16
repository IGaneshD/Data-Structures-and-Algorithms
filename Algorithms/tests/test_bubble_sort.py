import unittest
# Assuming Sorting/bubbleSort.py exists
from ..Sorting import bubbleSort

class TestBubbleSort(unittest.TestCase):

    def setUp(self):
        # Corrected: setUp (camelCase)
        self.arr = [5,4,3,2,1]
        self.sortObject = bubbleSort.Solution(self.arr)

    def tearDown(self):
        # Good practice for cleaning up resources
        super().tearDown()
    
    def test_sort(self):
        self.sortObject.sort()
        # Verify the list is correctly sorted
        self.assertEqual(self.sortObject.arr, [1,2,3,4,5])

    def test_sort1(self):
        self.sortObject.sort()
        # Verify the list is correctly sorted
        self.assertNotEqual(self.sortObject.arr, [1,2,3,4,4])

if __name__ == '__main__':
    unittest.main()
