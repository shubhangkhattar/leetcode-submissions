class Solution:
    def rob(self, nums: List[int]) -> int:

        rob_1, rob_2 = 0, 0

        for house in nums:
            temp = max(rob_1 + house,rob_2)
            rob_1 = rob_2
            rob_2 = temp
    
        return rob_2