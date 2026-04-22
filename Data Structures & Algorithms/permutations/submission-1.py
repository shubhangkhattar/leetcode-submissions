class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def dfs(bool_arr,curr_list):
            
            nonlocal result

            if len(curr_list) == len(nums):
                result.append(curr_list[:])
                return 

            for i in range(len(nums)):
                if bool_arr[i] == False:
                    bool_arr[i] = True
                    curr_list.append(nums[i])
                    dfs(bool_arr,curr_list)
                    curr_list.pop()
                    bool_arr[i] = False
            
        dfs([False]*len(nums),[])
        return result

                
