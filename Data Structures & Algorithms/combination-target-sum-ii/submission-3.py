class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []

        target_in_making = []

        def dfs(i,target):
            if target == 0:
                result.append(target_in_making[:])
                return 
            
            if i >= len(candidates) or target < 0:
                return

            target_in_making.append(candidates[i])
            dfs(i+1,target-candidates[i])
            target_in_making.pop()

            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i+1,target)

        dfs(0,target)
        return result



# 1,2,2,4,5,6,9
            

