#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        freqMap = {ch:0 for ch in s}
        counter = 0
        start,end ,head,d = 0,0,0,float("-inf")
        while(end<len(s)):
            if(s[end] in freqMap):
                freqMap[s[end]] +=1

                if(freqMap[s[end]] > 1):
                    counter+=1

            while(counter > 0):
                if end-start > d:
                    head = start
                    d = end-start
                print(start,end)
                if(s[start] in freqMap):

                    freqMap[s[start]] -=1
                    if(freqMap[s[start]] > 0):
                        counter-=1
                start+=1
            end+=1
            
        if end-start > d:
            d = end-start

        return d if d!=float('-inf') else 0