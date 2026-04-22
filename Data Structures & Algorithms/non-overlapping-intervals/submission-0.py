class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda pair: pair[0])

        end = intervals[0][1]

        count = 0

        for interval in intervals[1:]:
            if end > interval[0]:
                count += 1
                end = min(interval[1],end)
            else:
                end = interval[1]

        return count


