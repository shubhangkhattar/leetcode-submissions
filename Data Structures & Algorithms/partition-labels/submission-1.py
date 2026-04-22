class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_map = {}
        for i, char in enumerate(s):
            my_map[char] = i
        result = []
        size = 0
        end = 0
        for i, char in enumerate(s):
            end = max(end,my_map[char])
            size += 1

            if i == end:
                result.append(size)
                size = 0
        
        return result


