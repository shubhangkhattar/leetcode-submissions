class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList += [beginWord]
        adj = defaultdict(list)

        def isEdge(word1,word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count +=1
            return count == 1

        for word1 in wordList:
            for word2 in wordList:
                if isEdge(word1,word2):
                    adj[word1].append(word2)
                    adj[word2].append(word1)
        
        q = deque()
        
        q.append(beginWord)
        visited = set()
        steps = 1

        while q:
            q_len = len(q)
            for _ in range(q_len):
                word = q.popleft()
                visited.add(word)
                if word == endWord:
                    return steps
                for neighbor in adj[word]:
                    if neighbor not in visited:
                        q.append(neighbor)
            steps += 1

        return 0

