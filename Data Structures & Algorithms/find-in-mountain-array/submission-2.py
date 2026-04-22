class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 0
        r = mountainArr.length() - 1
        m = None
        while l <= r:
            m = (l + r) // 2
            midVal = mountainArr.get(m)
            midLeftVal = mountainArr.get(m-1)
            midRightVal = mountainArr.get(m+1)

            if midLeftVal < midVal < midRightVal:
                l = m + 1
            elif midLeftVal > midVal > midRightVal:
                r = m -  1
            else:
                break
        
        # Check Left
        l = 0
        r = m
        midLeftVal = mountainArr.get(l)
        midRightVal = mountainArr.get(r)
        if midLeftVal <= target <= midRightVal:

            while l <= r:
            
                m = (l + r) // 2

                midVal = mountainArr.get(m)

                if target > midVal:
                    l = m + 1
                elif target < midVal:
                    r = m - 1
                else:
                    return m
        # Check Right
        l = m + 1 #IMPORTANT
        r = mountainArr.length() - 1
        midLeftVal = mountainArr.get(l)
        midRightVal = mountainArr.get(r)
        if midLeftVal >= target >= midRightVal:

            while l <= r:
                m = (l + r) // 2

                midVal = mountainArr.get(m)

                if target < midVal:
                    l = m + 1
                elif target > midVal:
                    r = m - 1
                else:
                    return m
        
        return -1