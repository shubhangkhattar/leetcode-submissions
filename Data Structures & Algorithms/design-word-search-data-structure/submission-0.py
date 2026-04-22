class WordDictionary:

    def __init__(self):
        self.my_set = set()

    def addWord(self, word: str) -> None:
        self.my_set.add(word)

    def search(self, word: str) -> bool:
        for check_word in self.my_set:
            if len(word) > len(check_word):
                continue
            i = 0
            j = 0

            while i < len(check_word) and j < len(word):
                if check_word[i] != word[j] and word[j] != ".":
                    break
                i += 1
                j += 1

            if i == len(check_word) and j == len(word):
                return True
                
            
        return False
        
