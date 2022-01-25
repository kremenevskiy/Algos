from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        arr = [0] * (max(nums) + 1)
        for x in nums:
            arr[x] += x
        prev, curr = 0, 0
        for i in range(min(nums), len(arr)):
            prev, curr = curr, max(curr, prev + arr[i])
        return curr


print(Solution().deleteAndEarn([3,7,10,5,2,4,8,9,9,4,9,2,6,4,6,5,4,7,6,10]))
