class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        part = []

        def dfs(i):
            
            if i >= len(s):
                result.append(part.copy())
                return
            
            for j in range(i,len(s)):
                if isPali(i,j,s):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
            

        def isPali (l,r,s):
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True
                         
        dfs(0)
        print(result)
        return result