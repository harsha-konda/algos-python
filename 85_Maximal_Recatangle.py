# https://leetcode.com/problems/maximal-rectangle/
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        store = [[0 for _ in range(len(matrix[i]))] for i in range(len(matrix))]

        def largestHistogram(row):
            i = 0

            stack = []
            maxArea = 0

            while (i < len(row)):
                if (not stack or row[i] >= row[stack[-1]]):
                    stack.append(i)
                    i += 1
                else:
                    r_i = i - 1
                    curMax = stack.pop()
                    l_i = stack[-1] if stack else -1
                    maxArea = max(maxArea, row[curMax] * (r_i - l_i))
            while (stack):
                r_i = i - 1
                curMax = stack.pop()
                l_i = stack[-1] if stack else -1
                maxArea = max(maxArea, row[curMax] * (r_i - l_i))

            return maxArea

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                store[i][j] = 0 if matrix[i][j] == "0" else 1
                if i > 0 and matrix[i][j] == "1":
                    store[i][j] += store[i - 1][j]

        maxRectArea = 0
        for i in range(len(store)):
            rowArea = largestHistogram(store[i])
            maxRectArea = max(maxRectArea, rowArea)

        return maxRectArea
