# https://leetcode.com/problems/wiggle-subsequence/
class Solution:

    # Greedy Approach
    # O(n)
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if (not nums):
            return 0

        def getWiggle(findGreater):
            size = j = 1
            cur = nums[0]
            while (j < len(nums)):
                if ((findGreater and nums[j] > cur) or (not findGreater and nums[j] < cur)):
                    size += 1
                    cur = nums[j]
                    findGreater = not findGreater
                else:
                    cur = nums[j]

                j += 1
            return size

        size = max(getWiggle(True), getWiggle(False))

        return size

    # DP Approach
    #
