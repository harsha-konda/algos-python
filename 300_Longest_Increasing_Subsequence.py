# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

class Solution:

    # bottom up
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0 for _ in  nums]
        for i in range(0,len(nums)):
            dp[i] = 1
            for j in range(0,i):
                if(nums[i] > nums[j]):
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)