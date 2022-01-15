from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target-num], i]
            d[num] = i


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))




