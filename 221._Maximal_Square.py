# https://leetcode.com/problems/maximal-square/
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for _ in range(len(matrix[i]))] for i in range(len(matrix))]
        maxLen = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "1":
                    t = dp[i - 1][j] if i > 0 else 0
                    l = dp[i][j - 1] if j > 0 else 0
                    d = dp[i - 1][j - 1] if j > 0 and i > 0 else 0
                    dp[i][j] = min(t, l, d) + 1
                    maxLen = max(dp[i][j], maxLen)
        return maxLen ** 2
