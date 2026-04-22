class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        my_map = {}

        for i in range(len(s)):
            my_map[s[i]] = i

        result = []
        start = 0
        max_distance = 0
        for i,char in enumerate(s):
            max_distance = max(my_map[s[i]],max_distance)
            if i == max_distance:
                result.append(i-start+1)
                start = i+1
        return result
