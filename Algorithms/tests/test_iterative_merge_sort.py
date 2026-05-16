import pytest
import unittest
from ..Sorting.iterative_merge_sort import sort

def test_iterative_sort():
    assert sort([6,5,4,3,2,1]) == [1,2,3,4,5,6]
