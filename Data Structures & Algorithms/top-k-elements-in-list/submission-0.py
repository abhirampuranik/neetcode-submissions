class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 0

            res[i] += 1
        

        lists = sorted(res, key=res.get)

        return lists[::-1][:k]