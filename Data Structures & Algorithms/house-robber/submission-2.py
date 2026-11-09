class Solution:
    def rob(self, nums: List[int]) -> int:
        num_len = len(nums)
        total_so_far = [0] * num_len

        total_so_far[0] = nums[0]
        
        if num_len > 1:
            total_so_far[1] = max(nums[0], nums[1])

        i = 2
        while (i < len(nums)):
            total_so_far[i] = max(total_so_far[i-2]+nums[i], total_so_far[i-1])
            i += 1

        return total_so_far[-1]