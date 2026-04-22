class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def dfs(i,curr_list):
            
            nonlocal result

            if i == len(nums):
                result.append(curr_list[:])
                return 

            dfs(i+1, curr_list)
            curr_list.append(nums[i])
            dfs(i+1, curr_list)
            curr_list.pop()

        dfs(0,[])
        return result
            
            

            

            
            
                
