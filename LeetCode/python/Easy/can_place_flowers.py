from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, prev = 0, 0

        for cur in flowerbed:
            if cur == 1:
                if prev == 0:
                    count -= 1
                prev = 1
            else:
                if prev == 0:
                    count += 1
                    prev = 1
                else:
                    prev = 0
        return count >= n

print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))









