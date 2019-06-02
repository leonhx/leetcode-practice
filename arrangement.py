from typing import List, Tuple


# 输入
#   n
#   [..., (start_time_i, end_time_i), ...]
# timestamp int
#
# 条件:
# - 选择听一场后必须全程参加
# - 时间不能重叠
# - 不考虑切换成本
#
# 问题: 实现一个算法，找出最多能听多少场演唱会


def maxNumConcert(time_ranges: List[Tuple[int, int]]) -> int:
    time_ranges.sort(key=lambda x: x[1])
    result = 0
    last_et = 0
    for st, et in time_ranges:
        if st >= last_et:
            last_et = et
            result += 1
    return result
