# https://leetcode.com/problems/first-missing-positive/
from typing import List


class Solution:
    # O(n)
    # constant additional space
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        # eliminate all negative numbers
        i = 0
        while (i < len(nums)):
            if (nums[i]) <= 0:
                swap(i, len(nums) - 1)
                nums.pop()
            else:
                i += 1

        minima = 1
        maxima = len(nums)
        i = 0
        while (i < len(nums)):
            num = abs(nums[i])
            if (num >= minima and num <= maxima):
                nums[num - minima] = -abs(nums[num - minima])
            i += 1

        for i in range(len(nums)):
            if (nums[i] > 0):
                return i + minima

        return len(nums) + 1
