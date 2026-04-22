class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        n2 = 0 
        n1 = cost[n-1]
        for i in range(n-2,-1,-1):
            n1,n2 = min(n1+cost[i],n2+cost[i]),n1
            print(n1,n2)
        return min(n1,n2)

        # [1,2,3]
        #  - - 3 0
        #  3 2 3
            
        #  n1 n2