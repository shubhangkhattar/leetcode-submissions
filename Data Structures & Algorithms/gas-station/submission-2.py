class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        remaining_gas = 0
        result = 0
        for i in range(len(gas)):
            remaining_gas +=  gas[i] - cost[i]
            if remaining_gas < 0:
                result = i + 1
                remaining_gas = 0 

        return result