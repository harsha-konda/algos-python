#https://leetcode.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp = [0 for _ in range(len(s))]
        if(s[0]=='0'):
            return 0
        dp[0] = 1
        for i in range(len(s)):
            if i>0:
                if(s[i] =='0' and (int(s[i-1]+s[i]) > 26 or int(s[i-1]+s[i]) < 1)) :
                    return 0

                if(int(s[i-1]+s[i]) <=26 and s[i-1] != '0'):
                    dp[i] += (dp[i-2] if i > 1 else 1)

                if(s[i] !='0'):
                    dp[i] += dp[i-1]

        return dp[-1]
        