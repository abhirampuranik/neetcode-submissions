class Solution:
    def checkChar(self, c):
        if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('0') and ord(c) <= ord('9')):
            return True
        return False


    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if not self.checkChar(s[i]):
                i += 1
                continue

            if not self.checkChar(s[j]):
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True

            