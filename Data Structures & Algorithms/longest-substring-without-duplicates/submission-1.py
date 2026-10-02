class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maps = {}
        maxp = 0

        while r < len(s):
            if s[r] not in maps:
                maxp = max(maxp, r-l+1)
                maps[s[r]] = 1
                r += 1
            else:
                maps.pop(s[l], None)
                l += 1
        return maxp