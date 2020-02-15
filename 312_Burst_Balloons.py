# https://leetcode.com/problems/burst-balloons/
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        bset = set(list(range(len(nums))))
        cost = [i for i in nums]

        def recurse(bset):
            for i in bset:
                bset.remove(i)
                cost[i] =
