# Problem: Two Sum (Easy)
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, n in enumerate(nums):
            partner = target - n
            if partner in seen:
                return [seen[partner], i]
            seen[n] = i
