class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sortedS = "".join(sorted(word))
            if sortedS in anagrams:
                anagrams[sortedS].append(word)
            else:
                anagrams[sortedS] = [word]
        return list(anagrams.values())