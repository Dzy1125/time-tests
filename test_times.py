# -*- coding: utf-8 -*-
import pytest
from times import time_range, compute_overlap_time


# def test_given_input():
    
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

#     result = compute_overlap_time(large, short)
#     expected = [
#         ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
#         ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
#     ]
#     assert result == expected


# def test_no_overlap():
#     """测试两个时间段完全不重叠"""
#     range1 = time_range("2010-01-12 08:00:00", "2010-01-12 09:00:00")
#     range2 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
#     result = compute_overlap_time(range1, range2)
#     expected = [] 
#     assert result == expected


# def test_multiple_intervals_overlap():
    
#     range1 = time_range("2010-01-12 09:00:00", "2010-01-12 12:00:00", 3, 60)
#     range2 = time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 3, 60)
#     result = compute_overlap_time(range1, range2)
#     expected = [
#         ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
#         ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
        
# ]
#     assert result == expected


# def test_touching_intervals():
    
#     range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
#     range2 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
#     result = compute_overlap_time(range1, range2)
#     expected = []  
#     assert result == expected 

def test_time_range_backwards():
    """测试当end_time早于start_time时，程序应抛出ValueError"""
    with pytest.raises(ValueError, match="end_time must be after start_time"):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")