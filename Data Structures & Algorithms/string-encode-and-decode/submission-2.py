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
            num = int(num)
            word = ""
            char_to_read = i + num
            while (i<len(s) and i < char_to_read ):
                word += s[i]
                i+=1
            ans.append(word)



        return ans



            
        
