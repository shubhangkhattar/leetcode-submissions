class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals.sort(key=lambda x:x[0])

        start = intervals[0][0]
        end = intervals[0][1]

        result = []

        for i_start,i_end in intervals[1:]:
            if end >= i_start:
                end = max(end,i_end)
            else:
                result.append([start,end])
                start = i_start
                end = i_end

        result.append([start,end])

        return result