class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k+1):
            temp = prices[:]
            for source,destination,cost in flights:
                temp[destination] = min(temp[destination],cost+prices[source])
            prices = temp
        return prices[dst] if prices[dst] != float("inf") else -1

        

