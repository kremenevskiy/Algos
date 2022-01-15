from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]


print(Solution().singleNumber([2, 2, 1]))