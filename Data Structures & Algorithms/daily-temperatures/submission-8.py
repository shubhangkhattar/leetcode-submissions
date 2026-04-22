class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            last = stack[-1] if stack else i
            result.insert(0,last-i)
            stack.append(i)          
        return result


            
            
            

