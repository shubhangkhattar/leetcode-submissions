class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = nums.copy()

        for i in range(len(nums)):
            result[(i + k) % len(nums)] = nums[i]
        
        for i in range(len(nums)):
            nums[i] = result[i]