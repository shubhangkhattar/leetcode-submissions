class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        stack = []
        result = []

        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if not stack:
                result.append(0)
            else:
                result.append(stack[-1] - i)
            stack.append(i)
        
        return result[::-1]


