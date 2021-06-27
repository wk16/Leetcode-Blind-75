from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(start):
            if start>=len(nums)-2:
                if start==len(nums)-1:
                    return nums[start]
                return max(nums[start],nums[start+1])
            return max(nums[start]+dp(start+2), dp(start+1))
        return dp(0)

