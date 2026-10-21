from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies nums in-place to the next lexicographically greater permutation.
        """
        n = len(nums)

        # 1. Find the first index i from the right where nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. If found, find the smallest number to the right that is bigger than nums[i]
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # swap them

        # 3. Reverse the part after index i (this is the smallest arrangement of it)
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1