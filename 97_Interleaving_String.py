# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if(len(s1)+len(s2) != len(s3)):
            return False

        if(s1==s3 or s2==s3):
            return True

        dp = [[ False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dp[0][0] = True

        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i==0 and j==0:
                    continue

                if(i-1 > -1 and i-1 < len(s1) and s1[i-1] == s3[i+j-1]):
                    dp[i][j] = dp[i][j] or dp[i-1][j]

                if(j-1 > -1 and j-1 < len(s2) and s2[j-1] == s3[i+j-1]):
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        return dp[-1][-1]