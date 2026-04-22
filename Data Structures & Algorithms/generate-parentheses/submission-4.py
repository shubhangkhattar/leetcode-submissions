class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = set()

        def dfs(s,open,close):
            if open == close and len(s) == n*2:
                result.add(s)
                return
            elif close > open or len(s) > 2*n:
                return

            dfs(s + "(",open+1,close)
            dfs(s + ")",open,close+1)

        dfs("",0,0)
        print(result)
        return list(result)