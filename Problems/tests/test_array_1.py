import pytest
from Array.Find_Largest_Element import findLargest
from Array.Second_largest_element import secondLargestElementBruteForce

@pytest.mark.parametrize(["array", "largest_element"], [
    # Standard cases
    ([1, 2, 3, 4, 5], 5),
    ([10, 20, 5, 15], 20),
    
    # Unsorted/Random order
    ([9, 1, 8, 2, 7], 9),
    
    # Negative numbers
    ([-10, -5, -20, -1], -1),
    ([-5, 0, 5], 5),
    
    # Duplicate values
    ([7, 7, 7, 7], 7),
    ([1, 5, 5, 2], 5),
    
    # Single element
    ([42], 42),
    
    # Large numbers or Floats (if applicable)
    ([1.5, 2.7, 2.2], 2.7),
    ([10**6, 10**2, 10**7], 10**7),
])
def test_largestElement(array, largest_element):
    assert findLargest(array) == largest_element



def test_findLargest_empty():
    with pytest.raises(ValueError):
        findLargest([])



@pytest.mark.parametrize(["array", "result"],
                         [
                             ([1,2,3,4,5], 4),
                             ([1,2,3,5,5], 5),
                             ([5], -1),
                         ])
def test_secondLargest(array, result):
    assert secondLargestElementBruteForce(array) == result