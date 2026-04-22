class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s):
            open = 0
            for char in s:
                open += 1 if char == '(' else -1
                if open < 0:
                    return False
                    
            return not open

        def dfs(s):
            if len(s) == n*2:
                if valid(s):
                    res.append(s)
                return
            
            dfs(s+"(")
            dfs(s+")")

        dfs("")
        return res
