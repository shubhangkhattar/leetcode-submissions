class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def dfs(i,myList):
            if i == len(nums):
                nonlocal result
                result.append(myList[:])
                return
            dfs(i+1,myList)
            myList.append(nums[i])
            dfs(i+1,myList)
            myList.pop()
            return
        
        dfs(0,[])
        return result