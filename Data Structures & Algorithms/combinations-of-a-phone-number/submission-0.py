class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
            }

        result = []

        def dfs(i,curr_list):

            nonlocal result
            
            if i == len(digits):
                if curr_list:
                    result.append("".join(curr_list))
                return
            
            for letter in my_map[digits[i]]:
                curr_list.append(letter)
                dfs(i+1,curr_list)
                curr_list.pop()
        
        dfs(0,[])
        return result








