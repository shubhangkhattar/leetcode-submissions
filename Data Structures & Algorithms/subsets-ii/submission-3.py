class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(i,res):
            if i == len(nums):
                result.append(res[:])
                return 
            
            res.append(nums[i])
            dfs(i+1,res)
            res.pop()

            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
                
            dfs(i+1,res)

        dfs(0,[])
        return result

        1,1,2