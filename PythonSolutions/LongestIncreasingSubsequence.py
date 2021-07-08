from bisect import bisect_left
from typing import List


# O(N^2) Time
# O(N) Space
# Mine
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        for i in range(len(nums) - 1, -1, -1):
            maxInc = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if dp[j] + 1 > maxInc:
                        maxInc = dp[j] + 1
            dp[i] = maxInc
        res = 1
        for i in range(len(nums)):
            if dp[i] > res:
                res = dp[i]
        return res

    # Answer Keys
    # O(N^2) Time
    # O(N) Space
    # But faster in practice
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)

    # O(nLog(n)) Time
    # O(N) Space
    # Bisect is binary search module
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)

            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num

        return len(sub)
