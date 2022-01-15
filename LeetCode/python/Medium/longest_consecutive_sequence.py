from typing import List


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums = set(nums)
#         best = 0
#         for x in nums:
#             if x-1 not in nums:
#                 y = x+1
#                 while y in nums:
#                     y += 1
#                 best = max(best, y-x)
#         return best


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = dict()
        res = 0
        for num in nums:
            if num in d:
                continue
            if num+1 not in d and num-1 not in d:
                d[num] = 1
                res = max(res, d[num])
                continue
            elif num-1 not in d:
                r = d[num] = d[num + d[num+1]] = d[num+1] + 1
                res = max(res, r)
                continue
            elif num + 1 not in d:
                r = d[num] = d[num - d[num-1]] = d[num-1] + 1
                res = max(res, r)
                continue
            r = d[num + d[num + 1]] = d[num - d[num-1]] = d[num-1] + d[num+1] + 1
            d[num] = 1
            res = max(res, r)
        return res


a = [-2, -3, -3, 7, -3, 0, 5, 0, -8, -4, -1, 2]
print(Solution().longestConsecutive(a))


