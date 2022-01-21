from typing import List


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = {
#             0: 1,
#             1: 1,
#             2: 2
#         }
#         def climb(n):
#             if n in memo:
#                 return memo[n]
#             else:
#                 memo[n-1], memo[n-2] = climb(n-1), climb(n-2)
#                 return memo[n-1] + memo[n-2]
#         return climb(n)

# class Solution:
#     def climbStairs(self, n: int) -> int:
#
#         def climb(n):
#             if n <= 2:
#                 return n
#             if n not in memo:
#                 memo[n] = climb(n-1) + climb(n-2)
#             return memo[n]
#         memo = {}
#         return climb(n)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [1, 2]:
            return n
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 0, 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


print(Solution().climbStairs(4))