class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        my_stack = []
        
        n = len(temperatures)

        ans = [0]*n

        for i in range(n):
            
            while my_stack and temperatures[i] > temperatures[my_stack[-1]]:
                val = my_stack.pop()
                ans[val] = i - val

            my_stack.append(i)
                
        return ans

            

