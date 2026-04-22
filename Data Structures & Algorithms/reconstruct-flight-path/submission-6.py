class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)

        tickets.sort()

        for source,destination in tickets:
            adj[source].append(destination)


        path = []

        def dfs(city):
            nonlocal path

            path.append(city)

            if len(path) == len(tickets) + 1:
                return True
                
            temp = list(adj[city])
            for i,dest in enumerate(temp):
                adj[city].pop(i)
                if dfs(dest):
                    return True
                adj[city].insert(i,dest)
            path.pop()
            return False

        dfs("JFK")

        return path