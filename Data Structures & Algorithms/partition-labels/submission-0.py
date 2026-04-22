class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_map = {}
        for i, char in enumerate(s):
            my_map[char] = i
        
        left = 0
        right = 0
        n = len(s)

        result = []

        while right < n:
            max_distance = my_map[s[right]]
            
            while right <= max_distance:
                max_distance = max(my_map[s[right]], max_distance)
                right += 1
            
            result.append(right-left)
            left = right
            right = right
        
        return result

