class TrieNode:
    def __init__(self):
        self.children = [False]*26
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for i in range(len(word)):
            code = ord(word[i]) - ord('a')
            if not root.children[code]:
                root.children[code] = TrieNode()        
            root = root.children[code]
        root.endOfWord = True


    def search(self, word: str) -> bool:
        root = self.root
        for i in range(len(word)):
            code = ord(word[i]) - ord('a')
            if not root.children[code]:
                return False      
            root = root.children[code]
        return root.endOfWord
        

    def startsWith(self, prefix: str) -> bool:

        root = self.root
        for i in range(len(prefix)):
            code = ord(prefix[i]) - ord('a')
            if not root.children[code]:
                return False      
            root = root.children[code]
        return True
        
        