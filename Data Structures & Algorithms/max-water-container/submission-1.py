class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        maxv=0

        while l<r:
            h=min(nums[l],nums[r])
            b=r-l
            maxv=max(maxv, h*b)
            if nums[l]<nums[r]:
                l += 1
            else:
                r -=1

        return maxv
