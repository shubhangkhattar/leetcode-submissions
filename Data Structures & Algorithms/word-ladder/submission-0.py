class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def if_edge(word_1,word_2):
            count = 0
            for i in range(len(word_1)):
                if word_1[i] != word_2[i]:
                    count += 1
            
            return True if count == 1 else False

        graph = wordList + [beginWord]

        my_map = defaultdict(list)

        for i in range(len(graph)):
            for j in range(i+1,len(graph)):
                word_1 = graph[i]
                word_2 = graph[j]

                if if_edge(word_1,word_2):
                    my_map[word_1].append(word_2)
                    my_map[word_2].append(word_1)

        visited = set()
        q = deque()
        q.append(beginWord)

        steps = 1
        while q:
            n = len(q)
            
            for _ in range(n):
                word = q.popleft()
                visited.add(word)
                if word == endWord:
                    return steps
                for neighbor in my_map[word]:
                    if neighbor not in visited:
                        q.append(neighbor)
            steps += 1

        return 0