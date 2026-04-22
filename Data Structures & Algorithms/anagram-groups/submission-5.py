class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        my_dict = collections.defaultdict(list)

        for word in strs:
            alphaCount = [0]*26
            for char in word:
                alphaCount[ord(char) - ord("a")] += 1
            my_dict[tuple(alphaCount)].append(word)
        
        result = []

        return list(my_dict.values())
        
