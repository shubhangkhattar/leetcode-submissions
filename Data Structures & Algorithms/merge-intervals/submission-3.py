class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        intervals.sort()

        result = []

        start = intervals[0][0]
        end = intervals[0][1]

        for s,e in intervals:
            if end >= s:
                end = max(e,end)
            else:
                result.append([start,end])
                start = s
                end = e
        
        result.append([start,end])

        return result


        [[1,3],[1,5],[6,7]]