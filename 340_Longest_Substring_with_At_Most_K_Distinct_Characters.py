class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        store = {}
        low = 0
        ret = 0
        for i in range(len(s)):
            store[s[i]] = i
            if len(store) > k:
                low = min(store.values())
                del store[s[low]]
                low+=1
            ret = max(ret,i-low+1)
        return ret