class Solution:
    def minWindow(self, s: str, t: str) -> str:

        head,start,end,d = 0,0,0,float("inf")
        freqMap = {ch: 0 for ch in t}
        for ch in t:
            freqMap[ch] +=1

        counter = len(t)
        while(end< len(s)):
            curChar = s[end]
            if curChar in freqMap:
                if(freqMap[s[end]] > 0):
                    counter-=1
                freqMap[s[end]] -= 1
            end+=1

            while(counter == 0):
                if(end-start < d):
                    d = end-start
                    head = start
                if(s[start] in freqMap):
                    freqMap[s[start]] += 1
                    if freqMap[s[start]]>0:
                        counter += 1
                start+=1
        return s[head:head+d] if d!=float("inf") else ""

assert (Solution.minWindow("ADOBECODEBANC", "ABC") == "BANC")
assert (Solution.minWindow("AABC", "ABC") == "ABC")

# TODO:https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# TODO: https://leetcode.com/problems/longest-substring-without-repeating-characters/