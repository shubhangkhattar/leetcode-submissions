class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj_matrix = {c:[] for w in words for c in w}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            minLen = min(len(word1),len(word2))
            if word1[:minLen] == word2[:minLen] and len(word1) > len(word2):
                return ""
            for w in range(minLen):
                if word1[w] != word2[w]:
                    adj_matrix[word1[w]].append(word2[w])
                    break

        result = []
        visited = {}
        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True

            for neighbor in adj_matrix[char]:
                if dfs(neighbor):
                    return True
            
            result.append(char)
            visited[char] = False

            return False

        for c in adj_matrix:
            if dfs(c):
                return ""
    
        return "".join(result[::-1])