class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = 0

        if not nums2:
            return

        while l < m:
            if nums1[l] > nums2[0]:
                nums1[l],nums2[0] = nums2[0],nums1[l]
                r = 0
                while r < n-1:
                    if nums2[r] > nums2[r+1]:
                        nums2[r],nums2[r+1] = nums2[r+1],nums2[r]
                        r += 1
                    else:
                        break
            l += 1
        
        i = 0
        while i < n:
            nums1[l+i] = nums2[i]
            i += 1
        

        





        # nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2


        # 10,20,20,40,0,0

        # 1,2