class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        my_stack = []
        result = [0]*len(temperatures)

        for index in range(len(temperatures)):
            if my_stack:
                while my_stack and my_stack[-1][0] < temperatures[index]:
                    temperature, prev_index= my_stack.pop()
                    result[prev_index] = index-prev_index
            my_stack.append((temperatures[index],index))

        return result


         

         