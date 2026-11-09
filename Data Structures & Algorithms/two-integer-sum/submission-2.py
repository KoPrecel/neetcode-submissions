class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        known = {}
        index = 0
        while index < len(nums):
            num = nums[index]
            if num in known:
                return [known[num], index]
            else:
                known[target-num] = index
            index += 1
        return False