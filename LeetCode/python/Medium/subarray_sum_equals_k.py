from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        csum = 0
        d = {0: 1}
        for x in nums:
            csum += x
            cnt += d.get(csum-k, 0)
            d[csum] = d.get(csum, 0) + 1
        return cnt



print(Solution().subarraySum([-1, -1, 1], 0))