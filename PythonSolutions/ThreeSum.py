from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if i >= 1:
                if nums[i-1]==nums[i]:
                    continue
            l,r = i+1, len(nums)-1
            while l < r:
                total = num + nums[l]+nums[r]
                if total > 0:
                    r-=1
                elif total < 0:
                    l+=1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l-1]==nums[l]:
                        l+=1
        return ans