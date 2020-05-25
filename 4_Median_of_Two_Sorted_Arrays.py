from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:



        is_odd  = (len(nums1)+len(nums2))%2

        def cal_median(arr):
            if is_odd:
                return arr[len(arr)//2]
            else:
                return (arr[len(arr)//2-1]+arr[len(arr)//2])/2

        def binarySearch(i_start,i_end):
            i = (i_start+i_end)//2
            j = (len(nums1)+len(nums2)+1)//2 -i

            if not nums1:
                return cal_median(nums2)

            if not nums2:
                return cal_median(nums1)

            nums1_l,nums1_r = float('-inf'),float('inf')
            nums2_l,nums2_r = float('-inf'),float('inf')

            if i>0:
                nums1_l = nums1[i-1]

            if j>0:
                nums2_l = nums2[j-1]

            if i<len(nums1):
                nums1_r = nums1[i]

            if j<len(nums2):
                nums2_r = nums2[j]

            if nums1_l <= nums2_r and nums2_l <=nums1_r:
                if is_odd:
                    return max(nums1_l,nums2_l)
                else:
                    return (max(nums1_l,nums2_l)+min(nums1_r,nums2_r))/2

            if nums1_l>nums2_r:
                return binarySearch(i_start,i-1)
            else:
                return binarySearch(i+1,i_end)
        return binarySearch(0,len(nums1))

sol = Solution()
assert (sol.findMedianSortedArrays([1, 3],[2])==2.0)
assert (sol.findMedianSortedArrays([1, 2],[3,4])==2.5)
assert (sol.findMedianSortedArrays([1, 2,3,4,5],[3])==3.0)
assert (sol.findMedianSortedArrays([1, 2,3,4,5],[3])==3.0)
assert (sol.findMedianSortedArrays([1, 2,3,4,5],[])==3.0)