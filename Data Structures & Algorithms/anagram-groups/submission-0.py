class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap technique

        # the key should be ordered list(tuple) of 1's 0's of 26 alphabets

        final = {}


        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord('a')] += 1
            if tuple(count) not in final:
                final[tuple(count)] = []
            
            final[tuple(count)].append(s)
        
        return list(final.values())