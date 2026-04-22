class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for origin,destination in tickets:
            adj[origin].append(destination)

        result = []
        print(adj)
        def dfs(city):
            result.append(city)
            if len(result) == len(tickets) + 1:
                return True
            temp = adj[city].copy()
            for i,desitnation in enumerate(temp):
                adj[city].pop(i)
                if dfs(desitnation):
                    return True
                adj[city].insert(i,desitnation)
            result.pop()
            return False

        dfs("JFK")
        return result

