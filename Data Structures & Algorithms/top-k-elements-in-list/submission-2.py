class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = [[] for i in range(len(nums)+1)]

        res = {}

        for i in nums:
            res[i] = 1 + res.get(i, 0)
        
        for i in res:
            counter[res[i]].append(i)
        

        res = []
        # j = len(counter) - 1
        # while k > 0 and j > 0:
            
        #     if counter[j] != []:
        #         k -= 1

        #     for i in counter[j]:
        #         res.append(i)
        #     j -= 1

        for j in range(len(counter)-1, 0, -1):
            for i in counter[j]:
                res.append(i)
            if len(res) == k:
                break
            
        return res
        
        # res = {}
        # for i in nums:
        #     if i not in res:
        #         res[i] = 0

        #     res[i] += 1
        

        # lists = sorted(res, key=res.get)

        # return lists[::-1][:k]