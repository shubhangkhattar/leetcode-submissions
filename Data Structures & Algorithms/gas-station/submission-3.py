class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        remaining_gas = 0
        res = 0
        for i in range(len(gas)):
            remaining_gas += gas[i]
            remaining_gas -= cost[i]
            if remaining_gas < 0:
                res = i+1
                remaining_gas = 0

        return res

