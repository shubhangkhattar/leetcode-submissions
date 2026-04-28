class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        result = []

        def dfs(i,total,myList):

            if total > target or i > len(candidates):
                return

            if i == len(candidates):
                if total == target:
                    result.append(myList[:])
                return

            myList.append(candidates[i])
            dfs(i+1,total+candidates[i],myList)
            myList.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,total,myList)
                

        dfs(0,0,[])
        return result
