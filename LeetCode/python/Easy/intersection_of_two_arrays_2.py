from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        res = []

        for x in nums2:
            d[x] = d.get(x, 0) + 1

        for x in nums1:
            if x in d and d[x] > 0:
                res.append(x)
                d[x] -= 1
        return res