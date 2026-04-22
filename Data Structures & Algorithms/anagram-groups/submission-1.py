from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        my_map = defaultdict(list)

        for word in strs:            
            my_map[tuple(sorted(word))].append(word)

        return my_map.values()