class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        bool_arr = [False]*n
        result = []

        def dfs(res):
            if len(res) == len(nums):
                result.append(res[:])
                return


            for i in range(len(nums)):
                if bool_arr[i]:
                    continue
                bool_arr[i] = True
                res.append(nums[i])
                dfs(res)
                res.pop()
                bool_arr[i] = False

        dfs([])
        return result
