# -*- coding: utf-8 -*-
import pytest
from times import time_range, compute_overlap_time


def test_given_input():
    """原始样例测试"""
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
    ]
    assert result == expected


def test_no_overlap():
    """测试两个时间段完全不重叠"""
    range1 = time_range("2010-01-12 08:00:00", "2010-01-12 09:00:00")
    range2 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    result = compute_overlap_time(range1, range2)
    expected = []  # 不重叠，应返回空列表
    assert result == expected


def test_multiple_intervals_overlap():
    """测试两个时间段各自包含多个区间"""
    range1 = time_range("2010-01-12 09:00:00", "2010-01-12 12:00:00", 3, 60)
    range2 = time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 3, 60)
    result = compute_overlap_time(range1, range2)
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
        
]
    assert result == expected


def test_touching_intervals():
    """测试两个时间段首尾相接但不重叠"""
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range2 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    result = compute_overlap_time(range1, range2)
    expected = []  # 恰好接触但不重叠
    assert result == expected
