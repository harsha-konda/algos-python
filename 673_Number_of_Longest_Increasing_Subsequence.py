#https://leetcode.com/problems/number-of-longest-increasing-subsequence/
from typing import List

class Solution:

    # bottom up
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [(0,0) for _ in  nums]
        for i in range(0,len(nums)):
            dp[i] = (1,1)
            for j in range(0,i):
                if(nums[i] > nums[j]):
                    if(dp[i][0] == dp[j][0] +1):
                        dp[i][1] += dp[j][1]
                    else:
                        dp[i] = (max(dp[i][0] ,dp[j][0]),1)

        return max(dp,key = lambda k:k[0])[1]