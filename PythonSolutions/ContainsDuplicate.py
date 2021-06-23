from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for num in nums:
            if num in mp:
                return True
            mp[num] = 1
        return False