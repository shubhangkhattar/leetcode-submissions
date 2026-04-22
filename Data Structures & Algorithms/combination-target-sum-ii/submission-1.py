class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        result = set()

        def dfs(i,curr_list,total):

            nonlocal result

            if total == target:
                result.add(tuple(curr_list[:]))
                return 

            if total > target or i == len(nums):
                return 
            
            dfs(i+1,curr_list,total)

            total += nums[i]
            curr_list.append(nums[i])
            dfs(i+1,curr_list,total)
            curr_list.pop()

        dfs(0,[],0)
        return [list(i) for i in result]