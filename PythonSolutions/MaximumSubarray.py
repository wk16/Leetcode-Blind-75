from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = 0
        total = 0
        for val in nums:
            total += val
            if total >= max_val:
                max_val = total
            elif total < 0:
                total = 0
        if max_val ==0:
            return max(nums)
        return max_val