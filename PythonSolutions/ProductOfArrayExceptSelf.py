from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums0 = 0
        total = 1
        ans = []
        for num in nums:
            if num == 0:
                nums0 += 1
            else:
                total *= num
        if nums0 >= 2:
            return [0] * len(nums)
        for num in nums:
            if num == 0:
                ans.append(total)
            elif nums0 == 1:
                ans.append(0)
            else:
                ans.append(total // num)
        return ans
