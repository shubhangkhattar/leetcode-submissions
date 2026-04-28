class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        for num in nums:
            for result in results[:]:
                results.append(result + [num])
                

        return results