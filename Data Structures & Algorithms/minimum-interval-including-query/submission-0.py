class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = [-1] * len(queries)
        for i,query in enumerate(queries):
            min_d = float("inf")
            for left,right in intervals:
                if left <= query <= right:
                    min_d = min(right-left+1,min_d)
            if min_d != float("inf"):
                result[i] = min_d

        return result