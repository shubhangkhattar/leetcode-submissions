class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        n = len(costs)
        n1 = costs[-1]
        n2 = 0

        for i in range(n-2,-1,-1):
            n1,n2 = min(n1+costs[i],n2+costs[i]),n1
        return min(n1,n2)


                    
        # 1, 2, 3
        #    2  0
        #    n1 n2
                 