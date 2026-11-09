class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}

        for n in nums:
            if n in numsDict:
                return True
            else:
                numsDict[n] = 0

        return False