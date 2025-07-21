from find_sum import find_largest_sum
import pytest

def test_output_only_single_digits():
    assert find_largest_sum(['1', '4', '7']) == 7

def test_output_multiple_digits():
    assert find_largest_sum(['12', '34', '56']) == 11

def test_output_mixed_digits():
    assert find_largest_sum(['1a2b', '3c4d', '5e6f']) == 11