from typing import List
from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        AB = Counter(a + b for a in nums1 for b in nums2)
        return sum(AB[-c-d] for c in nums3 for d in nums4)


print(Solution().fourSumCount([0,1,-1], [-1,1,0], [0,0,1], [-1,1,1]))