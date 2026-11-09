class Solution:
    def rob(self, nums: List[int]) -> int:
        total_so_far = [0] * len(nums)

        if len(nums) >= 1:
            total_so_far[0] = nums[0]
        
        if len(nums) >= 2:
            total_so_far[1] = max(nums[0], nums[1])

        n = 2
        while n < len(nums):
            total_so_far[n] = max(total_so_far[n-2] + nums[n], total_so_far[n-1])
            n += 1
        
        return total_so_far[-1]

# [1,1,3,3]

# cannot steal from two houses in a row
# how do we maximize the profit as a robber

# input = list of non-negative integers
# output = integer

# dynamic programming

# base case
# if len(nums) == 1
#     -> nums[0]
# if len(nums) == 2
#     -> max(nums[0], nums[1])
# if len(nums) > 3
#     -> max(total_so_far[n-2] + num[n], total_so_far[n-1])