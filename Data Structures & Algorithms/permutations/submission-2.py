class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def dfs(bool_arr,curr_list):
            if len(curr_list) == len(nums):
                result.append(curr_list[:])
                return
            
            for i in range(len(nums)):
                if not bool_arr[i]:
                    bool_arr[i] = True
                    curr_list.append(nums[i])
                    dfs(bool_arr,curr_list)
                    bool_arr[i] = False
                    curr_list.pop()
            

        dfs([False]*len(nums),[])
        return result