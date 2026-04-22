class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def if_edge(word1,word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
            if count == 1:
                return True
            return False
        
        graph = [beginWord] + wordList
        
        my_map = defaultdict(list)

        for i in range(len(graph)):
            for j in range(i+1,len(graph)):
                if if_edge(graph[i],graph[j]):
                    my_map[graph[i]].append(graph[j])
                    my_map[graph[j]].append(graph[i])

        q = deque()
        q.append(beginWord)
        steps = 0
        
        visited = set()

        while q:
            steps += 1
            q_len = len(q)
            for _ in range(q_len):
                word = q.popleft()
                if word == endWord:
                    return steps
                visited.add(word)
                for neighbor in my_map[word]:
                    if neighbor not in visited:
                        print("I was here")
                        q.append(neighbor)
            
            
        return 0

        








