from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = 0
        prof = 0
        for i in range(1, len(prices)):
            low = min(low, prices[i])
            prof = max(prof, prices[i] - low)
        return prof

print(Solution().maxProfit([5, 10, 4, 12]))


