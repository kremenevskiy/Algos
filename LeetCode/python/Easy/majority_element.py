from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = nums[0], 1
        for i in range(1, len(nums)):
            if count == 0:
                count += 1
                major = nums[i]
            elif nums[i] == major:
                count += 1
            else:
                count -= 1
        return major
