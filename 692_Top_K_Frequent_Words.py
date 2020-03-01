# https://leetcode.com/problems/top-k-frequent-words/
from heapq import *

class Solution:
    # Hash Map
    # O(nlgn)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        wordsDict = {}
        for word in words:
            if word in wordsDict:
                wordsDict[word] +=1
            else:
                wordsDict[word] = 1

        words = sorted([(k,v) for k,v in wordsDict.items()],key=lambda kv:(-kv[1],kv[0]))

        return [word[0] for word in words[:k]]

    # HashMap + Queue
    # O(nlgk)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        wordsDict = {}
        for word in words:
            if word in wordsDict:
                wordsDict[word] +=1
            else:
                wordsDict[word] = 1

        wordArr = [[] for i in range(len(words))]

        heap = []

        for key,value in wordsDict.items():
            heappush(heap,(-value,key))

        result = [heappop(heap)[1] for _ in  range(k)]

        return result

    # Bucket Sort
    # O(n)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        wordsDict = {}
        for word in words:
            if word in wordsDict:
                wordsDict[word] +=1
            else:
                wordsDict[word] = 1

        wordArr = [[] for i in range(len(words))]

        for key,v in wordsDict.items():
            wordArr[v].append(key)

        i = k
        j = len(wordArr)-1
        result = []

        while(i>=0 and j>=0):
            if wordArr[j]:
                wordArrJ = sorted(wordArr[j])
                result += wordArrJ
                i -= len(wordArrJ)
            j-=1
        return result[:k]
