class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        known_s = {}
        known_t = {}
        
        for letter in s:
            if letter in known_s:
                known_s[letter] += 1
            else:
                known_s[letter] = 1

        for letter in t:
            if letter in known_t:
                known_t[letter] += 1
            else:
                known_t[letter] = 1
        
        return known_s == known_t