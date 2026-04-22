class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        max_reach = 0
        for i in range(len(nums)-1):
            if max_reach < i + nums[i]:
                jumps += 1
                max_reach = i + nums[i]
                if max_reach >= len(nums) - 1:
                    return jumps
        
        return jumps
                    
        # [2,4,1,1,1,1]
        #  2       