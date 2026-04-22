class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        candidates.sort()
        
        result = []

        def dfs(i,subset,total):
            if total == 0:
                result.append(subset[:])
                return
            
            if total < 0 or i >= len(candidates):
                return

            subset.append(candidates[i])
            dfs(i+1,subset,total-candidates[i]) 
            subset.pop()

            while i < len(candidates)-1 and candidates[i+1] == candidates[i]:
                i += 1

            dfs(i+1,subset,total)

        dfs(0,[],target)
        return result


        
        # [1,2,2,4,5,6,9]
        # [1,2,]