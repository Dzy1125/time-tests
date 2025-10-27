
from times import time_range, compute_overlap_time
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    # 实际运行结果
    result = compute_overlap_time(large, short)

    # 期望结果（你可以先运行 times.py 把输出复制过来）
    expected = expected = [
    ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
    ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
]
      
    # 比较两者是否一致
    assert result == expected
