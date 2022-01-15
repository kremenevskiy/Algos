from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right, mid = 0, len(nums), 0
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left






# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums)
#         mid = 0
#         while (right - left) > 1:
#             mid = right - (right - left) // 2
#             if target == nums[mid]:
#                 return mid
#             if target > nums[mid]:
#                 left = mid
#             else:
#                 right = mid
#
#         if nums[left] > target and left - 1 == -1:
#             return 0
#         if target == nums[left]:
#             return left
#         return left - 1 if nums[left] > target else left + 1


