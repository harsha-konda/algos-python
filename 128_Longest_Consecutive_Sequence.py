# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List


class Solution:
    # naive O(nlg)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        i = 0

        lcs = 0
        while (i < len(nums)):
            cs = 0
            j = i
            while (j + 1 < len(nums) and nums[j + 1] == nums[j] + 1):
                j += 1
            cs = j - i + 1
            lcs = max(cs, lcs)
            i = j + 1
        return lcs

    # T(2n)
    # go to minima and start count cs from theron
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {num: False for num in nums}

        def getMinima(map, val):
            minima = val
            while (minima - 1 in map):
                minima -= 1
            return minima

        def iterateFromMinima(map, val):
            length = 1
            if map[val]:
                return length

            map[val] = True
            while (val + 1 in map):
                map[val + 1] = True
                length += 1
                val += 1
            return length

        lcs = 0
        for val in map:
            if map[val]:
                continue
            else:
                minima = getMinima(map, val)
                cs = iterateFromMinima(map, val)
                lcs = max(cs, lcs)

        return lcs

    # O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {num: False for num in nums}
        lcs = 0
        for val in map:
            if map[val]:
                continue
            else:
                l_i, l_val = 0, val
                r_i, r_val = 0, val

                while (l_val - 1 in map):
                    map[l_val - 1] = True
                    l_i += 1
                    l_val -= 1

                while (r_val + 1 in map):
                    map[r_val + 1] = True
                    r_i += 1
                    r_val += 1

                cs = l_i + r_i + 1
                lcs = max(cs, lcs)

        return lcs
