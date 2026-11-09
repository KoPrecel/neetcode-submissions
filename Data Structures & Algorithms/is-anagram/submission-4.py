class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sdict = {}
        tdict = {}

        for letter in s:
            if letter not in sdict:
                sdict[letter] = 1
            else:
                sdict[letter] += 1
            
        for letter in t:
            if letter not in tdict:
                tdict[letter] = 1
            else:
                tdict[letter] += 1

        for index in sdict:
            if index in tdict:
                if sdict[index] == tdict[index]:
                    continue
                else:
                    return False
            else:
                return False
        
        return True
