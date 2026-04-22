class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flight_map = defaultdict(list)

        tickets.sort()

        for source,destination in tickets:
            flight_map[source].append(destination)
        

        res = ["JFK"]
        def dfs(city):
            
            if len(res) == len(tickets) + 1:
                return True

            if city not in flight_map:
                return False
        

            temp = list(flight_map[city])
            for i, destination in enumerate(temp):
                flight_map[city].pop(i)
                res.append(destination)
                if dfs(destination):
                    return True
                flight_map[city].insert(i,destination)
                res.pop()

            return False

        dfs("JFK")
        return res