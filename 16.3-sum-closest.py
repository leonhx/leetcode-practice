#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    def __init__(self, *, debug=False):
        super().__init__()
        self.debug = debug

    def binarySearchClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return None
        if target <= nums[0]:
            return nums[0]
        if target >= nums[-1]:
            return nums[-1]
        mid_i = len(nums) // 2
        mid_v = nums[mid_i]
        if target == mid_v:
            return target
        elif target < mid_v:
            x = self.binarySearchClosest(nums[:mid_i], target)
        else:
            x = self.binarySearchClosest(nums[mid_i + 1:], target)
        return mid_v if not x or abs(target - mid_v) < abs(target - x) else x

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if self.debug:
            print(nums)
        closest = sum(nums[-3:])
        for i in range(len(nums)):
            if nums[i] * 3 > max([closest, target]):
                break
            for j in range(i + 1, len(nums) - 1):
                sij = nums[i] + nums[j]
                if sij + nums[j] > max([closest, target]):
                    break
                tgt = target - sij
                x = self.binarySearchClosest(nums[j + 1:], tgt)
                if self.debug:
                    print(f'given {nums[i]}, {nums[j]}, find {tgt}, get {x}')
                if x:
                    candidate = sij + x
                    if candidate == target:
                        return candidate
                    if abs(target - candidate) < abs(target - closest):
                        if self.debug:
                            print(f'{nums[i]} + {nums[j]} + {x}')
                        closest = candidate
        return closest
