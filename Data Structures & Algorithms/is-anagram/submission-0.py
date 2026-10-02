class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dicts = {}
        dictt = {}
        for i in range(len(s)):
            if s[i] not in dicts:
                dicts[s[i]] = 0
            dicts[s[i]] += 1

            if t[i] not in dictt:
                dictt[t[i]] = 0
            dictt[t[i]] += 1

        for i in dicts:
            if i not in dictt:
                return False
            if dicts[i] != dictt[i]:
                return False
        return True