from functools import lru_cache
class Solution:
    @lru_cache(maxsize=30)
    def helper(self, n):
            if n==2:
                return 2
            elif n == 1:
                return 1
            else:
                total = self.helper(n-1)+self.helper(n-2)
                return total
    def climbStairs(self, n: int) -> int:
        return self.helper(n)