class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def dfs(i,curr):
            if i == len(nums):
                result.append(curr[:])
                return

            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            
            while i < len(nums)-1 and nums[i+1] == nums[i]:
                i += 1
        
            
            dfs(i + 1,curr) 

           
            
                
        dfs(0,[])
        return result
                