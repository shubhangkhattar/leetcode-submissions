class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
         l = 0
         r = len(arr) - 1


         while l <= r:
            if r - l + 1 == k:
                return arr[l:r+1]
            
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1
        

#  k = 2
#  x = 6


#         [2,4,5,8]
#          0 1 2 3 



#          l = 0
#          r = 3