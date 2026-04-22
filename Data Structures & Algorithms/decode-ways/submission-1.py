class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        
        mem = [-1]*n

        def dfs(i):
            
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            
            
            count = 0
            if mem[i] != -1:
                count += mem[i] 
            else:

                count += dfs(i+1)

                if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                    count += dfs(i + 2)

            mem[i] = count

            return count

        return dfs(0)



