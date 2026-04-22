class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word))+"#"+word

        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_list = []
        
        i = 0
        print(s)
        while i < len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1
            i+= 1
            decoded_list.append(s[i:i+int(count)])
            i = i + int(count)


        return decoded_list