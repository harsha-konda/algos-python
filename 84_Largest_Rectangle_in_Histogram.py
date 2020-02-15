# https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List


class Solution:
    # naive  O(n^3)
    # A simple solution is to one by one consider all bars as starting points and calculate area
    # of all rectangles starting with every bar. Finally return maximum of all possible areas.
    def largestRectangleAreaBrute(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                minHeight = heights[i]
                for k in range(i, j + 1):
                    minHeight = min(minHeight, heights[k])

                maxArea = max(maxArea, minHeight * ((j - i) + 1))
        return maxArea

    # naive O(n^2)
    def largestRectangleAreaBrute(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            minHeight = heights[i]
            for j in range(i, len(heights)):
                minHeight = min(minHeight, heights[j])
                maxArea = max(maxArea, minHeight * ((j - i) + 1))
        return maxArea

    # stack based O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        i = 0
        while (i < len(heights)):
            if (not stack or heights[i] >= stack[-1]):
                stack.append(heights[i])
                i += 1
            else:
                r_i = i - 1
                curMax = stack.pop()
                l_i = stack[-1] if stack else 0
                maxArea = max(maxArea, heights[curMax] * (r_i - l_i))

        while (stack):
            r_i = i - 1
            curMax = stack.pop()
            l_i = stack[-1] if stack else 0
            maxArea = max(maxArea, (r_i - l_i + 1) * heights[curMax])

        return maxArea
