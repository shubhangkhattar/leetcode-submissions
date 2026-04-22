class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            count = len(string)
            result += str(count) + "#" + string

        return result


    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        result = []

        while i < len(s):
            inner_string = ""
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1

            count = int(count)
            i += 1
            j = i
            while j < i + count:
                inner_string += s[j]
                j += 1
            result.append(inner_string)
            i = j
        
        return result




            
