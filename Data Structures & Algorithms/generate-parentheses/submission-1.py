class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s,open,close):
            if open == close and len(s) == 2*n:
                res.append(s)
                return 
            elif close > open or len(s) > 2*n:
                return

            dfs(s+"(",open+1,close)
            dfs(s+")",open,close+1)

        dfs("",0,0)
        return res
