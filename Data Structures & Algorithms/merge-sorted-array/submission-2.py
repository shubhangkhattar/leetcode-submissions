class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if not nums2:
            return

        s1 =  0

        while s1 < m:
            if nums1[s1] > nums2[0]:
                nums1[s1],nums2[0] = nums2[0],nums1[s1]
                i = 0
                while i+1 < n and nums2[i] > nums2[i+1]:
                    nums2[i+1],nums2[i] = nums2[i],nums2[i+1]
                    i += 1  
            s1 += 1

        i = 0
        while s1 < m + n:
            nums1[s1] = nums2[i]
            i += 1
            s1 += 1
        



        # [1,2,10,20,0,0], 
        
        # [20,40], n = 2


