/*
 * @lc app=leetcode id=1 lang=swift
 *
 * [1] Two Sum
 */
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        for i in nums.indices {
            for j in (i + 1)..<nums.count {
                if nums[i] + nums[j] == target {
                    return [i, j]
                }
            }
        }
        return []
    }
}
