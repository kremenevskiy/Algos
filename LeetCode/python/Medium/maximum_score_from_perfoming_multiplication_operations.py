from typing import List
from functools import lru_cache


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * m+1 for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                dp[i][left] = max(mult * nums[left] + dp[i+1][left+1],
                                  mult * nums[right] + dp[i+1[left]])
print(Solution().maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))

