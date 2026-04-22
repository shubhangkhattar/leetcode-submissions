class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        print(n)
        memo = [[-1] * (target + 1) for _ in range(n)]

        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            
            memo[i][target] = (dfs(i + 1, target) or 
                               dfs(i + 1, target - nums[i]))
            return memo[i][target]

        dfs(0, target)

        for row in memo:
            print("\t\t\t".join(map(str,row)))

        return memo[0][target]