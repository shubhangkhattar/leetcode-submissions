class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for word in strs:
            msg += f'{len(word)}#{word}'
        return msg

    def decode(self, s: str) -> List[str]:
        msg = []
        i = 0
        while i < len(s):
            digit = ""
            
            while i < len(s) and s[i] != "#":
                digit += s[i]
                i += 1
            
            digit = int(digit)

            msg.append(s[i+1:i + digit + 1])
        
            i += digit + 1

        return msg

            


