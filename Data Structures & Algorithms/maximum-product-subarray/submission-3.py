class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_product = nums[0]
        max_product = nums[0]
        result = nums[0]

        for num in nums[1:]:
            tmp = max_product * num
            max_product = max(max_product*num,min_product*num,num)
            min_product = min(min_product*num,tmp,num)
            result = max(max_product,result)
        return result


