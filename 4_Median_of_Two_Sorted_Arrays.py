from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        is_odd = (len(nums1) + len(nums2)) % 2

        def search(start1, end1, start2, end2):

            mid1 = (start1 + end1) // 2
            mid2 = (start2 + end2) // 2

            def left_ele(mid1, mid2):
                return max(nums1[mid1], nums2[mid2])

            def right_ele(mid1, mid2):
                return min(nums1[mid1 + 1], nums2[mid2 + 1])

            if (nums1[mid1] > nums2[mid2 + 1]):
                return search(start1, mid1, start2, end2)
            elif (nums2[mid2] > nums1[mid1 + 1]):
                return search(start1, end1, start2, mid2)
            else:
                total_left_digits = mid1 + 1 + mid2 + 2
                total_right_digits = (len(nums1) - 1) - mid1 + (len(nums2) - 1) - mid2
                print(is_odd, total_left_digits, total_right_digits)
                if (not is_odd and total_left_digits == total_right_digits):
                    print("going")
                    return (left_ele(mid1, mid2) + right_ele(mid1, mid2)) / 2.0

                if (is_odd):
                    if (total_left_digits + 1 == total_right_digits):
                        return left_ele(mid1, mid2)
                    elif (total_left_digits == total_right_digits + 1):
                        return right_ele(mid1, mid2)

        return search(0, len(nums1) - 1, 0, len(nums2) - 1)
