class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        def dfs(i,curr):
            if i == len(nums):
                result.add(tuple(curr[:]))
                return
                
            dfs(i + 1,curr)

            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
                
        dfs(0,[])
        return [list(x) for x in result]
                