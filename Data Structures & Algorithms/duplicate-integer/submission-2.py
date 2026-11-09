class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        known = {}
        for num in nums:
            if num in known:
                return True
            known[num] = num
        return False
        