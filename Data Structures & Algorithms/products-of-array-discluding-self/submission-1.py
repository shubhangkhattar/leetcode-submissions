class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        pre = [1] * (len(nums))
        post = [1] * (len(nums))
        n = len(nums)
        
        pre_num = 1
        post_num = 1

        for i in range(n):
            pre[i] = pre_num
            post[n-i-1] = post_num
            pre_num *= nums[i]
            post_num *= nums[n-i-1]

        for i in range(n):
            res[i] = pre[i] * post[i]

        return res