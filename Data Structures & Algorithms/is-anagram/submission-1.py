class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False
        
        my_map1 = {}
        my_map2 = {}

        for word in s:
            my_map1[word] = my_map1.get(word,0) + 1
        
        for word in t:
            my_map2[word] = my_map2.get(word,0) + 1

        return my_map1 == my_map2