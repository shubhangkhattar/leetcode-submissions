class Solution:
    def rob(self, nums: List[int]) -> int:
        h1 = 0
        h2 = nums[0]

        for num in nums[1:]:
            h1,h2 = h2,max((h1+num),h2)
        return h2

      
    #   0 1,1,3,3
    #       i j 
    #       1 4 