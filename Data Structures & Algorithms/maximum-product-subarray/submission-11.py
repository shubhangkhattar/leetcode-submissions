class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxProduct = nums[0]
        minProduct = nums[0]
        result = float("-inf")
        for num in nums[1:]:
            temp = maxProduct
            maxProduct = max(maxProduct*num,minProduct*num,num)
            minProduct = min(temp*num,minProduct*num,num)
            result = max(maxProduct,result)

        return -1 if result == float("-inf") else result


        

        #      [-3,-3,-3,  -3]
        # Max = -3  9. -3
        # Min = -3  -3  -27 81
