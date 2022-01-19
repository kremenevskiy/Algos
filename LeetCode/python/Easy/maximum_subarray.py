from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prevsum = nums[0]
        sum = nums[0]
        zerod = False
        for i in range(1, len(nums)):
            if nums[i] < 0 and abs(nums[i]) > sum:
                if sum > prevsum:
                    prevsum = sum
                if nums[i] > sum:
                    sum = nums[i]
                    continue
                sum = nums[i]
                zerod = True
                continue
            if nums[i] >= 0 and sum < 0:
                sum = nums[i]
                continue
            if nums[i] < 0:
                if sum > prevsum:
                    prevsum = sum
                if nums[i] > sum:
                    sum = nums[i]
                    continue
            sum += nums[i]
            zerod = False
        if zerod:
            if sum > 0:
                return max(prevsum, sum)

        return max(prevsum, sum)



print(Solution().maxSubArray([-2, -3, -1]))

