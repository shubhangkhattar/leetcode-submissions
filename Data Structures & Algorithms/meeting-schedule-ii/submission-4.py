"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        interval_s = sorted([interval.start for interval in intervals])
        interval_e = sorted([interval.end for interval in intervals])

        n = len(intervals)

        s = 0
        e = 0
        count = 0
        ans = 0

        while s < n:
            if interval_s[s] < interval_e[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            
            ans = max(count,ans)
        
        return ans
            