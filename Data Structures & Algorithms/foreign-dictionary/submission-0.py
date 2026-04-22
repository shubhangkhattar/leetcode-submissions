class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {c: set() for w in words for c in w}
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            min_length = min(len(word1),len(word2))

            if word1[:min_length] == word2[:min_length] and len(word2) < len(word1):
                return ""

            for j in range(min_length):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        visited = {} # False Visited , True Visited and in Path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True
            for nei in adj[char]:
                if dfs(nei):
                    return True

            res.append(char)
            visited[char] = False
            


        for char in adj.keys():
            if dfs(char):
                return ""
        
        return "".join(res[::-1])