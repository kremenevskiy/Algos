from typing import List


class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        if n == 0:
            return t0
        elif n in [1, 2]:
            return t1
        for i in range(0, n - 2):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t2


print(Solution().tribonacci(25))


"""
0 1 1 -> 2 -> 4 -> 7 -> 13

"""