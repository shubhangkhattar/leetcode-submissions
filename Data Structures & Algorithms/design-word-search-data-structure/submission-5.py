class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr_node = self.root
        for s in word:
            if s not in curr_node.children:
                curr_node.children[s] = TrieNode()
            curr_node = curr_node.children[s]
        curr_node.endOfWord = True
            
                
    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            if j == len(word):
                return root.endOfWord

            if word[j] == ".":
                for child in root.children.values():
                    if dfs(j + 1, child):
                        return True
            else:
                if word[j] in root.children:
                    return dfs(j + 1, root.children[word[j]])

            return False


        return dfs(0,self.root)



        

        
