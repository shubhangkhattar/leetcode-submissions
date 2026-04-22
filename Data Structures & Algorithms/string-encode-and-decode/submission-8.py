class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for word in strs:
            encode += str(len(word)) + "#" + word
        return encode

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1

            num = int(num)
            start = 1 + i
            end = i + num + 1
            result.append(s[start:end])
            i = end
        
        return result   





