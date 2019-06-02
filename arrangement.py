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
    if not time_ranges:
        return 0
    time_ranges.sort(key=lambda x: x[1])
    result = [time_ranges[0]]
    i = 1
    while i < len(time_ranges):
        last_st, last_et = result[-1]
        if time_ranges[i][0] >= last_et:
            result.append(time_ranges[i])
        i += 1
    return len(result)
