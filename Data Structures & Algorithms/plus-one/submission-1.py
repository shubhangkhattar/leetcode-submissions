class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(digits)-1,-1,-1):
            digit =  digits[i] + carry
            carry = digit // 10
            digit = digit % 10
            digits[i] = digit
        
        if carry:
            digits.insert(0,carry)
        
        return digits


