from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        
        for word in strs:
            freq_map = [0]*26
            for char in word:
                freq_map[ord(char) - ord('a')] += 1
            my_map[tuple(freq_map)].append(word)
        
        result = []

        for value in my_map.values():
            result.append(value)

        return result