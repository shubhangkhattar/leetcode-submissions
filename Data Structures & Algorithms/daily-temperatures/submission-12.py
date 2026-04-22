class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop() 
            else:
                stack.append(i)
        
        return result

        # [30,38,30,36,35,40,28]
        #  0  1  2  3  4   5  6

        # (),(),(),(),(),(),(0)