class Solution:
    def canJump(self, nums: List[int]) -> bool:
        to_reach = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i] >= to_reach:
                to_reach = i
        
        return to_reach == 0