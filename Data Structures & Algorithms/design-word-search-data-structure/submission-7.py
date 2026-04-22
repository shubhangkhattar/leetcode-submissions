class TrieNode:
    def __init__(self):
        self.children = [False] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        root = self.root
        for char in word:
            code = ord(char) - ord("a")
            if not root.children[code]:
                root.children[code] = TrieNode()
            root = root.children[code]
        root.endOfWord = True

        

    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            if j == len(word):
                return root.endOfWord

            if word[j] == ".":
                for child in root.children:
                    if child and dfs(j+1,child):
                        return True
                return False

            code = ord(word[j]) - ord("a")
            if not root.children[code]:
                return False
            return dfs(j+1,root.children[code])

        return dfs(0,self.root)

    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)