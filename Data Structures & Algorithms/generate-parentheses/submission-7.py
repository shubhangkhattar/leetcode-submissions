class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(open,close,curr_list):



            if close > open:
                return

            if len(curr_list) == 2*n:
                if open == close:
                    result.append("".join(curr_list[:]))
                return
            
            curr_list.append("(")
            dfs(open+1,close,curr_list)
            curr_list.pop()
            curr_list.append(")")
            dfs(open,close+1,curr_list)
            curr_list.pop()

        dfs(0,0,[])
        print(result)
        return result
