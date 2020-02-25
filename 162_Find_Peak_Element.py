class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def recurseFindPeakElement(low,high):
            if(low == high):
                return low

            mid = (low+high)//2

            if(nums[mid] > nums[mid+1]):
                return recurseFindPeakElement(low,mid)
            else:
                return recurseFindPeakElement(mid+1,high)

        return  recurseFindPeakElement(0,len(nums)-1)

    def findPeakElement(self, nums: List[int]) -> int:

        low = 0
        high = len(nums)-1

        while(low < high):
            mid = (low+high)//2
            if(nums[mid] > nums[mid+1]):
                high = mid
            else:
                low = mid+1

        return low

