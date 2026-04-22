class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n_number = 0
        for num in nums:
            xor=xor^num^n_number
            n_number+=1

        xor = xor^n_number
        return xor
