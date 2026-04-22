class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        my_stack = []
        
        n = len(temperatures)

        ans = [0]*n

        for i in range(n-1,-1,-1):
            if not my_stack:
                my_stack.append(i)
            else:
                while my_stack and temperatures[my_stack[-1]] <= temperatures[i]:
                    my_stack.pop()
                if my_stack:
                    ans[i] = my_stack[-1] - i
                my_stack.append(i)
                
        return ans

            

