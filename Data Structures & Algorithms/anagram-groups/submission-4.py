from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for word in strs:
            count_array = [0]*26

            for char in word:
                 count_array[ord(char)-ord('a')] += 1
            
            my_dict[tuple(count_array)].append(word)
        
        result = list(my_dict.values())

        return result

        
            
