class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry_over = 0
        
        digits[-1] += 1
        n = len(digits)

        for i in range(n-1,-1,-1):
            
            digits[i] += carry_over
            carry_over = digits[i] // 10
            digits[i] %= 10

            if carry_over == 0:
                return digits

        if carry_over:
            digits.insert(0,carry_over)
        
        return digits
        
        
