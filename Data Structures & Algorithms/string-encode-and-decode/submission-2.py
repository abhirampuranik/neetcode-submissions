class Solution:
    def __init__(self):
        self.splitter = "$$$"

    def createstring(self, s):
        return "\""+s+"\""+self.splitter

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += self.createstring(s)
        
        return res


    def decode(self, s: str) -> List[str]:
        strs = s.split(self.splitter)
        strs.pop()
        res = []
        for s in strs:
            res.append(s[1:-1])

        return res