#https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self, s, wordDict):
        store = [None for _ in s]
        def dfs(end):
            if end < 0 :
                return True
            if store[end] is not None:
                return store[end]
            
            for i in range(end,-1,-1):
                if s[i:end+1] in wordDict and dfs(i-1):
                    store[end] = True
                    return True 
            store[end] = False 
            return False
        
        return dfs(len(s)-1)


