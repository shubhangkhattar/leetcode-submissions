class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        min_val, max_val = nums[0], nums[0]
        result = nums[0]
        for num in nums[1:]:
            temp = max(min_val*num,max_val*num,num)
            print(temp)
            min_val = min(min_val*num,max_val*num,num)
            max_val = temp
            result = max(max_val,result)
        return result


# nums=[2,3,-2,4]
# min.=   2
# max = 2
