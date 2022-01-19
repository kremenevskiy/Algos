from typing import List

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         @cache
#         def solve(i, must_pick):
#             if i >= len(nums): return 0 if must_pick else -inf
#             return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
#         return solve(0, False)


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         big, sum = float('-inf'), 0
#         for i in range(n):
#             sum += nums[i]
#             big = max(big, sum)
#             if sum < 0:
#                 sum = 0
#         return big


class Solution:
    def maxSubArray(self, nums):
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)



print(Solution().maxSubArray([-2, 1]))

