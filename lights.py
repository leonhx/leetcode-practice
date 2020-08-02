_init_lights = [0, 1, 0, 0, 1, 0, 1, 0]

# 方案一

def get_next_day(lights):
    new_lights = [0]
    for i in range(1, len(lights) - 1):
        if lights[i - 1] == lights[i + 1]:
            new_lights.append(1)
        else:
            new_lights.append(0)
    new_lights.append(0)
    return new_lights


def solution1(n_days):
    result = _init_lights
    for _ in range(n_days):
        result = get_next_day(result)
    return result


# 方案二
# 由于8个灯最多只有2**6 == 64种状态（首尾两盏灯必定是一直关着的），并且每一种状态的下一状态都是确定的，因此必定会存在循环。
# 通过运行代码发现：第14天的状态与初始状态相同

# 将这14种状态预先存下来
_day_lights = [_init_lights]
for i in range(1, 14):
    _day_lights.append(get_next_day(_day_lights[i - 1]))


def solution2(n_days):
    return _day_lights[n_days % 14]
