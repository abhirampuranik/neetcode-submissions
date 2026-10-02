class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        res = []
        for i in range(len(nums)):
            if nums[i] in dict1:
                res = [dict1[nums[i]], i]
                break
            dict1[target-nums[i]] = i
        return res