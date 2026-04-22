class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0 
        ans = []
        while (i < len(s)):
            num = ''
            while s[i] != '#':
                num += s[i]
                i += 1
            i += 1
            length = int(num)
            word = s[i:i + length]
            ans.append(word)
            i += length  
        return ans



            
        
