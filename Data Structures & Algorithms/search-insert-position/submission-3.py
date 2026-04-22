class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m-1
            else:
                l = m+1        
        return l

        # target = 5

        # [-1,0,2,4,6,8]
        #   0 1 2 3 4 5
        #         |
        #           |
        #           |
