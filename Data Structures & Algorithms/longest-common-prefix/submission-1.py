class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        max_length = 0
        word = ""

        result = ""

        for word in strs:
            if max_length > len(word):
                max_length = len(word)
                word = word
        
        for i in range(len(word)):
            char = word[i]
            for word in strs:
                if i < len(word) and word[i] == char:
                    continue
                else:
                    return result
            result += char

        return result


            
