class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        n = len(words)
        
        adj = {c:[] for w in words for c in w}

        for i in range(n-1):           
            word1 = words[i]
            word2 = words[i+1]
            
            minLen = min(len(word1),len(word2))

            if word1[:minLen] == word2[:minLen] and len(word2) < len(word1):
                return ""

            for w in range(minLen):
                if word1[w] != word2[w]:
                    adj[word1[w]].append(word2[w])
                    break

        result = []
        visited = {}

        def dfs(char):

            if char in visited:
                return visited[char]

            visited[char] = True

            for i in adj[char]:
                if dfs(i):
                    return True
            
            visited[char] = False
            result.append(char)
            return  visited[char]
        
        for w in adj:
            if dfs(w):
                return ""


        return "".join(result)[::-1]