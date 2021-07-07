from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, minProd, maxProd = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            tempMax = max(num, num * minProd, num * maxProd)
            minProd = min(num, num * minProd, num * maxProd)
            maxProd = tempMax
            res = max(res, maxProd)
        return res