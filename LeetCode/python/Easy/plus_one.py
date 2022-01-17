from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        inc = []
        taken = 1
        for i in range(len(digits)-1, -1, -1):
            if taken:
                if digits[i] + taken > 9:
                    taken = 1
                    digits[i] = 0
                else:
                    digits[i] += 1
                    taken = 0
        if taken:
            digits.insert(0, 1)
        return digits





for i in range(5, -1, -1):
    print(i)