from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = min(height[0], height[n-1]) * (n-1)
        l = 0
        r = n - 1
        while l <= r and r >= l:
            if height[l] < height[r]:
                curr = l + 1
                while height[curr] < height[l]:
                    curr += 1
                l = curr
            else:
                curr = r - 1
                while height[curr] < height[r]:
                    curr -= 1
                r = curr
            area = max(area, min(height[l], height[r]) * (r - l))
        return area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
