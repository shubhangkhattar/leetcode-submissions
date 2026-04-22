from collections import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l,r = 0, len(arr) - 1

        while r - l + 1 > k:
            if abs(arr[r]-x) >= abs(arr[l]-x):
                r -= 1
            else:
                l += 1
        
        return arr[l:r+1]



        # [2,4,5,8]
        #  0 1 2 3
        #  4,2,1,3
        #  l.    r
         