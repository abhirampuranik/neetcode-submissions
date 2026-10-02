class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        l = 0
        r = 1
        maxp = 0

        while l < len(nums) - 1:
            maxp = max(maxp, nums[r] - nums[l])
            r += 1

            if r >= len(nums):
                l += 1
                r = l+1
        return maxp
        
