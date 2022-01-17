from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1

        if n > 0:
            nums1[:n] = nums2[:n]


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         left = m - 1
#         right = n - 1
#         key = len(nums1) - 1
#
#         while left >= 0 and right >= 0:
#             if nums1[left] < nums2[right]:
#                 nums1[key] = nums2[right]
#                 right -= 1
#                 key -= 1
#             else:
#                 nums1[key] = nums1[left]
#                 left -= 1
#                 key -= 1
#
#         while right >= 0:
#             nums1[key] = nums2[right]
#             right -= 1
#             key -= 1

