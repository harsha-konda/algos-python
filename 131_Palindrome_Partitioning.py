class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[None for _ in s] for _ in s]
        
        results = []
        
        def isPalindrome(start,end):
            i,j = start,end
            if dp[i][j] is not None:
                return dp[i][j]
            
            while(i<=j):
                if s[i] != s[j]:
                    dp[i][j] = False
                    return False
                i+=1
                j-=1
            dp[start][end] = True
            return dp[start][end]    
                
        def getPartitions(start,seq):
            if start == len(s):
                results.append(seq.copy())
            for end in range(start,len(s)):
                if isPalindrome(start,end):
                    seq.append(s[start:end+1])
                    getPartitions(end+1,seq)
                    seq.pop()
                
        getPartitions(0,[])
        return results