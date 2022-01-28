from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        if m > n:
            m, n = n, m
            text1, text2 = text2, text1
        dp = [[0] * (n + 1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[j] == text2[i]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j], dp[i+1][j], dp[i][j+1])
        return dp[m][n]

print(Solution().longestCommonSubsequence('abcabddc', 'aacddbdc'))