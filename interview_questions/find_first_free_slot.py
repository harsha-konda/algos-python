"""
intervals = [
[(1,2),(3,4)],
[(1,3),(3,6)],
[(1,4),(4,5),(7,9)],
]

"""

from heapq import *

def getFirstFreeInterval(intervals):

	heap = []
	p = [0 for _ in intervals]

	for i in range(len(intervals)):
		heappush(heap,(intervals[i][0],i))


	interval,_ = heap[0]
	union_interval = (interval[0],interval[0])

	while(heap):
		interval,i = heappop(heap)
		p[i]+=1
		j = p[i]

		if interval[0] > union_interval[1]:
			return (union_interval[1],interval[0])

		union_interval = (union_interval[0],max(interval[1],union_interval[1]))

		if j < len(intervals[i]):
			heappush(heap,(intervals[i][j],i))


intervals1 = [
[(1,2),(3,4)],
[(1,3),(3,6)],
[(1,4),(4,5),(7,9)],
]
		
assert(getFirstFreeInterval(intervals1)==(6,7))
