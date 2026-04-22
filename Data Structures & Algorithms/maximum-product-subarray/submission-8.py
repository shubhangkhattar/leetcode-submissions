class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        min_product = nums[0]
        max_product = nums[0]
        result = nums[0]

        for num in nums[1:]:
            temp = max_product
            max_product = max(max_product*num,min_product*num,num)
            min_product = min(num,min_product*num,temp*num)
            result = max(max_product,result)
            print(min_product,max_product,result)
        
        return result
         