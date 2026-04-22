class Solution:
    def isHappy(self, n: int) -> bool:

        my_set = set()

        while n not in my_set:
            my_set.add(n)
            digits = [int(digit) for digit in list(str(n))]
            print(digits)
            n = 0
            for digit in digits:
                n += pow(digit,2)

            if n == 1:
                return True
            

        return False
