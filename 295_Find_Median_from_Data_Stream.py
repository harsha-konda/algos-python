# https://leetcode.com/problems/find-median-from-data-stream/
from heapq import *


# Naive
# O(nlgn) insertion
# O(1) median
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        sorted(self.nums)

    def findMedian(self) -> float:
        is_even = len(self.nums) % 2 == 0
        mid = len(self.nums) // 2
        if is_even:
            median = (self.nums[mid] + self.nums[mid - 1]) / 2
        else:
            median = self.nums[mid]
        return median


class MedianFinder:
    def __init__(self):
        self.l_max_heap, self.r_min_heap = [], []

    def addNum(self, num: int) -> None:
        heappush(self.l_max_heap, -num)
        heappush(self.r_min_heap, -heappop(self.l_max_heap))
        if (len(self.l_max_heap) < len(self.r_min_heap)):
            heappush(self.l_max_heap, -heappop(self.r_min_heap))

    def findMedian(self) -> float:
        median = (-self.l_max_heap[0] + self.r_min_heap[0]) / 2.0 if len(self.l_max_heap) == len(self.r_min_heap) else - \
            self.l_max_heap[0]
        return median
