class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = 1

        while r < len(nums):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
            r += 1
        
        print(nums)
        
        return l
    
        # 2, 10, 10, 30, 30, 30
        #         |
        #            r

    # 0 1 2 1 1 2 2 3 3 4
    #       l
    #               r




