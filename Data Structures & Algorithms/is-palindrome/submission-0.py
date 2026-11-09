class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            lchar = s[l]
            rchar = s[r]
            if not lchar.isalnum():
                l += 1
                continue
            if not rchar.isalnum():
                r -= 1
                continue
            if lchar.lower() == rchar.lower():
                l += 1
                r -= 1
            else:
                return False
        return True
        