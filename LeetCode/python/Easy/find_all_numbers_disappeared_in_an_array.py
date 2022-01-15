from typing import List

# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         s = set(range(1, len(nums) + 1))
#         for num in nums:
#             if num in s:
#                 s.remove(num)
#         return s


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            index = abs(num) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i, num in enumerate(nums) if num > 0]
