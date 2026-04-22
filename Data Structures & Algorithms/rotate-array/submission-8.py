class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0 
        r = len(nums) - 1

        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        

        k = k % len(nums)

        l = 0 
        r = k - 1

        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1

        l = k
        r = len(nums) - 1

    
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1





        # k = 4

        # 0 1 2 3 
        # 1,2,3,4,
        
        # 4 5 6 7
        # 5,6,7,8


# [1,2,3,4,5,6,7,8]

# [1,2,3,4,5,6,7,8]

# [8,1,6,5,4,3,2,7]

# [8,1,2,3,4,5,6,7]