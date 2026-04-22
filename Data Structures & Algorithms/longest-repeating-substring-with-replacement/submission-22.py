import heapq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            count, maxf = {},0
            for j in range(i,n):
                count[s[j]] = count.get(s[j],0)+1
                maxf = max(count[s[j]],maxf)
                if (j - i + 1) - maxf <= k:
                    res = max(res,(j - i + 1))
        return res
