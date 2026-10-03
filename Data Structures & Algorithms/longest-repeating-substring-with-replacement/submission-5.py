class Solution:
    # at any point in time / window, the map can have 2 keys, with one of them having value max of k
    # if map have more than 2 keys or neither of the values are less than or equal to k, reduce left window
    # max length string is 2 keys's value's sum
    def valuesGreater(self, nums, k):
        if len(nums) < 1:
            return False
        maxv = max(nums)
        sums = sum(nums)
        com = sums - maxv
        if com > k:
            return True
        return False

    def characterReplacement(self, s: str, k: int) -> int:
        maps = {}
        l,r = 0, 0
        maxC = 0

        while r < len(s):

            if s[r] not in maps:
                maps[s[r]] = 0
            maps[s[r]] += 1
            r += 1
 
            while self.valuesGreater(list(maps.values()), k):
                maps[s[l]] -= 1
                if maps[s[l]] == 0:
                    maps.pop(s[l], None)
                l += 1

            length = sum(maps.values())
            maxC = max(maxC, length)
        
        return maxC



# class Solution:
#     def valuesGreater(self, nums, k):
#         if len(nums) < 1:
#             return False
#         maxv = max(nums)
#         sums = sum(nums)
#         com = sums - maxv  # Total replacements needed = window_len - max_freq
#         if com > k:
#             return True
#         return False

#     def characterReplacement(self, s: str, k: int) -> int:
#         maps = {}
#         l, r = 0, 0
#         maxC = 0

#         while r < len(s):
#             # 1. Expand right window first
#             maps[s[r]] = maps.get(s[r], 0) + 1
#             r += 1

#             # 2. Shrink left window if replacements needed exceed k
#             while self.valuesGreater(list(maps.values()), k):
#                 maps[s[l]] -= 1
#                 if maps[s[l]] == 0:
#                     del maps[s[l]]
#                 l += 1

#             # 3. Update max valid window size
#             length = sum(maps.values())
#             maxC = max(maxC, length)

#         return maxC