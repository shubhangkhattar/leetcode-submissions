class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.endOfWord = True

        

    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            if j == len(word):
                return root.endOfWord

            if word[j] == ".":
                for child in root.children.values():
                    if dfs(j+1,child):
                        return True
                return False

            if word[j] not in root.children:
                return False
            return dfs(j+1,root.children[word[j]])

        return dfs(0,self.root)

    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)