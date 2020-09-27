# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
"""
Intuition:
For each candidate left bound equal to some value in some array, let's determine the next-rightmost value of each array. 
If it doesn't exist, then our left is already too large for any subsequent candidates to have a solution.
 Otherwise, we can choose the maximum of these to be the corresponding right bound for our candidate left bound.
  We take the maximum of all such candidates.
"""
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        breakLoop = False
        minHeap = []
    
        for i in range(len(nums)):
            heappush(minHeap,(nums[i][0],i,0))
        
        breakLoop = False
        result = None
        maxima = max([nums[i][0] for i in range(len(nums))])
    
        while(minHeap):
            val,i,j = heappop(minHeap)
            minima = val
            if not result or maxima - minima < result[1] - result[0]:
                result = [minima,maxima]

            if j+1 >= len(nums[i]):
                return result
            maxima  = max(maxima,nums[i][j+1])
            heappush(minHeap,(nums[i][j+1],i,j+1))