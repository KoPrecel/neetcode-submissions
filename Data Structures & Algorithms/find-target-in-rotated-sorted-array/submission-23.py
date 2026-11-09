class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3,4,5,6,1,2]
        #        l r
        #        m

        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2

        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
     
        if nums[right] < nums[left]:
            while left < right:
                if left == middle:
                    pivot = left
                    break
                if nums[left] < nums[middle]:
                    left = middle
                elif nums[left] > nums[middle]:
                    right = middle
                middle = (left + right) // 2

            if nums[0] <= target <= nums[pivot]:
                left = 0
                right = pivot
            else:
                left = pivot + 1
                right = len(nums) - 1
            middle = (left + right) // 2

        # [3,5,6,0,1,2]

        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1

        return -1