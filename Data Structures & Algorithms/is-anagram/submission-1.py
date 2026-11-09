class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sdict = {}
        tdict = {}
        for letter in s:
            if letter in sdict:
                sdict[letter] += 1
            else:
                sdict[letter] = 1

        for letter in t:
            if letter in tdict:
                tdict[letter] += 1
            else:
                tdict[letter] = 1
        
        for i in sdict:
            if i in tdict:
                if sdict[i] == tdict[i]:
                    continue
                else:
                    return False
            else:
                return False

        return True