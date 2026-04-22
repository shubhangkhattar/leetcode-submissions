class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total//2

        dp = [[False] * (target + 1) for _ in range(len(nums)+1)]

        for i in range(len(dp)):
            dp[i][0] = True
        
        # print(dp)

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j] = dp[i-1][j]
                if nums[i-1] <= j:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]

        print(dp)
        return dp[-1][-1]


    #      0 1 2 3 4
    #    0 T F F F F 
    #    1 T 
    #    2 T
    #    5 T

    # T
    # F
        
        # target = 
        


        #   0 1 2 3 4 5
        # 0 T F F F F F
        # 1 T T F F F F
        # 2 T T T T F F 
        # 3 T T T T T T
        # 4 T T T T 


    
