from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def dp(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                i += 1
                j += 1
                return 1 + dp(i, j)
            else:
                return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)
