class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        dict1 = {nums[0]: 0}
        for i in range(1, len(nums)):
            value = dict1.get(target - nums[i])
            if value != None:
                return [value, i]
            dict1[nums[i]] = i
