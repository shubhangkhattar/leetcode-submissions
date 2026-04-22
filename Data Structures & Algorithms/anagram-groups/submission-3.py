class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        
        
        for string in strs:
            
            freq_map = [0]*26
            for char in string:
                freq_map[ord(char) - ord("a")] += 1
            my_map[tuple(freq_map)].append(string)

        return [x for x in my_map.values()]



