from typing import List


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n in [1, 2]:
#             return max(nums[0], nums[1]) if n == 2 else nums[0]
#         dp = [0] * n
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])
#         for i in range(2, n):
#             dp[i] = max(dp[i-2] + nums[i], dp[i-1])
#         return dp[-1]
#
#
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def dp(i):
#             if i == 0:
#                 return nums[0]
#             if i == 1:
#                 return max(nums[0], nums[1])
#             if i not in memo:
#                 memo[i] = max(dp(i-1), dp(i-2) + nums[i])
#             return memo[i]
#         memo = {}
#         return dp(len(nums)-1)


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n in [1, 2]:
            return max(nums[0], nums[1]) if n == 2 else nums[0]
        dp2 = nums[0]
        dp1 = max(nums[0], nums[1])
        dp = 0
        for i in range(2, n):
            dp = max(dp1, dp2 + nums[i])
            dp2 = dp1
            dp1 = dp
        return dp

print(Solution().rob([1, 3, 1, 3, 100, 200]))