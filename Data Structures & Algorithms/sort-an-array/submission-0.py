class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr,l,m,r):
            
            new_arr = []
            
            p1 = l
            p2 = m+1

            while p1 <= m and p2 <= r:
                if arr[p1] <= arr[p2]:
                    new_arr.append(arr[p1])
                    p1 += 1
                else:
                    new_arr.append(arr[p2])
                    p2 += 1
            
            while p1 <= m:
                new_arr.append(arr[p1])
                p1 += 1
            
            while p2 <= r:
                new_arr.append(arr[p2])
                p2 += 1
            
            p1 = l

            while p1 <= r:
                arr[p1] = new_arr[p1-l]
                p1 += 1

        def mergeSort(arr,l,r):
            
            if l == r:
                return arr
            
            m = (l+r) // 2
            mergeSort(arr,l,m)
            mergeSort(arr,m+1,r)
            merge(arr,l,m,r)
    
        mergeSort(nums,0,len(nums)-1)
        return nums






