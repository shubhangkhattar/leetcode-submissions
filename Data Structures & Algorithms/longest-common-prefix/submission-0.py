class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs[1:]:
                print(char) 
                print(word)
                if len(word)-1 < i or char != word[i]:
                    return ans
            ans += char
            
        return ans
                
                

        



