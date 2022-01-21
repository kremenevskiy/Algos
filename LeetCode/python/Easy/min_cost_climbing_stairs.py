from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        d2 = cost[0]
        d1 = cost[1]

        for i in range(2, n):
            d = min(d2 + cost[i], d1 + cost[i])
            d2 = d1
            d1 = d
        return min(d2, d1)


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         def dp(i):
#             if i == 0:
#                 return cost[0]
#             if i == 1:
#                 return cost[1]
#             if i not in memo:
#                 memo[i] = min(dp(i-1) + cost[i], dp(i-2) + cost[i])
#             return memo[i]
#
#         memo = {}
#         return min(dp(len(cost)-1), dp(len(cost)-2))
