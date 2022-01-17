from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         d = dict()
#         for x in nums:
#             if x in d:
#                 return True
#             d[x] = 1
#         return False
