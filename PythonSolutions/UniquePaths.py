from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(maxsize=None)
        def dp(m, n):
            if m < 1 or n < 1:
                return 0
            if m == 1 or n == 1:
                return 1
            return dp(m - 1, n) + dp(m, n - 1)
        return dp(m, n)