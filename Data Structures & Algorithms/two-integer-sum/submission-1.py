class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rdict = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in rdict:
                return [rdict[diff], i]
            else:
                rdict[n] = i