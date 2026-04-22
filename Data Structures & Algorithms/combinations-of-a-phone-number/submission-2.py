class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        my_map = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz",}
       
        result = []

        def dfs(i,res):
            if len(res) == len(digits):
                result.append("".join(res))
                return

            for char in my_map[digits[i]]:
                res.append(char)
                dfs(i+1,res)
                res.pop()
            
        dfs(0,[])
        return result
