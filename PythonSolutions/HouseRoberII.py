class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def robHouses(nums):
            Rob, non_Rob = 0, 0
            for n in nums:
                non_Rob, Rob = max(non_Rob, Rob), non_Rob + n
            return max(Rob, non_Rob)

        return max(robHouses(nums[:-1]), robHouses(nums[1:]))
