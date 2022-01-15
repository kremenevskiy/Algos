from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        for i, num in enumerate(nums):
            if num == 0:
                cnt += 1
            else:
                nums[i-cnt] = num
        for i in range(cnt):
            nums[-1 - i] = 0



