class Solution:
    def isHappy(self, n: int) -> bool:
        my_set = set()


        while n not in my_set:
            my_set.add(n)
            temp = 0
            while n > 0:

                digit = n%10
                n = n//10
                temp += (digit*digit)
            print(temp)
            n = temp
            if temp == 1:
                return True
        print(my_set)
        return False


