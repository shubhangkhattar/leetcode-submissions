class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r = max(nums), sum(nums)

        res = r

        def canSplit(largest):
            subArray = 0
            curSum = 0

            for n in nums:
                curSum += n
                if curSum > largest:
                    curSum = n
                    subArray += 1
            
            return True if subArray + 1 <= k else False

        while l <= r:
            
            m = (r + l) // 2
            
            if canSplit(m):
                r = m-1
                res = min(m,res)
            else:
                l = m+1
        
        return res