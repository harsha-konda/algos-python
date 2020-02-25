"""
Question:
Given a string aaaabbbbbaaabbaa
Where a represents forest, b represents land
And k number of cuts u can make
So that try to cut down the trees to maximize the land area
"""

class Solution:
    def getMaximumLandArea(self,s, k):
        i=0
        store = []
        print(1)
        def compute_length(start,ch):
            end = start
            while(end<len(s) and s[end] == ch):
                end+=1
            store.append((end-start,ch))
            return end

        while(i<len(s)):
            if(s[i] == 'a'):
                end = compute_length(i,'a')
            else:
                end = compute_length(i,'b')
            i = end
        print(store)


Solution().getMaximumLandArea("aaaaabaaaaababaaaa",1)