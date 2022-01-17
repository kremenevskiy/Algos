from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                nums[i - count] = nums[i]
        return len(nums) - count



arr = [1,2,3,4,4,5]
print(Solution().removeDuplicates(arr))
print(arr)
