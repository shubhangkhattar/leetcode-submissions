class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_time = [float("inf")] * n
        flight_time[src] = 0
        for _ in range(k+1):
            temp = flight_time[:]

            for source,destination,cost in flights:
                temp[destination] = min(temp[destination],flight_time[source]+cost)

            flight_time = temp
        return -1 if flight_time[dst] == float("inf") else flight_time[dst]
