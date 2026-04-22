class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        my_map = {}
        for i,char in enumerate(s):
            my_map[char] = i
        
        print(my_map)
        
        start,end = 0,my_map[s[0]]
        for i in range(len(s)):
            end = max(my_map[s[i]],end)
            if i == end:
                result.append(end-start+1)
                start = i+1
        return result
                   
        # 0 1 2 3 4 5 6 7 8 9 10 11 12  
        # x y x x y z b z b b i  s  l
        
s = 0
e = 4
        # x


