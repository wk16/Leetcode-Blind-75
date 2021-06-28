from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                current=num
                currentStreak=1
                while current+1 in nums:
                    current+=1
                    currentStreak+=1
                longest=max(currentStreak,longest)
        return longest