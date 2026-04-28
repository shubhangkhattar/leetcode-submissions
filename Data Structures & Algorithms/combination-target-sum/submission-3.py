class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def dfs(i,total,myList):


            
            if i == len(nums):
                if total == target:
                    nonlocal result
                    result.append(myList[:])
                return

            if total > target:
                return

            dfs(i+1,total,myList)
            
            myList.append(nums[i])            
            dfs(i,total+nums[i],myList)
            myList.pop()

        dfs(0,0,[])
        return result
            


