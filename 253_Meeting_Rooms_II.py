#https://leetcode.com/problems/meeting-rooms-ii/

from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key=lambda i:(i[0],i[1]))

        i=0
        intervalHeap = [0]
        cost= 1
        while(i<len(intervals)):
            if intervals[i][0] >= intervalHeap[0]:
                val = heappop(intervalHeap)
                heappush(intervalHeap,intervals[i][1])
            else:
                cost+=1
                val = heappush(intervalHeap,intervals[i][1])
            i+=1

        return cost if len(intervals) >0  else 0
