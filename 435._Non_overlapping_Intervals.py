# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedIntervals = sorted(intervals, key=lambda x: (x[1]))

        def overlap(i1, i2):
            return (i2[1] - i1[0]) < ((i1[1] - i1[0]) + (i2[1] - i2[0]))

        i = 0
        prev = None

        cost = 0
        while (i < len(sortedIntervals)):
            is_overlapping = False
            if prev:
                is_overlapping = is_overlapping or overlap(prev, sortedIntervals[i])

            if is_overlapping:
                cost += 1
            else:
                prev = sortedIntervals[i]

            i += 1
        return cost
