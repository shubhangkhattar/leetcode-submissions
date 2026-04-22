class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        


        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False
        
        def dfs(i,j,k):
            if k == n3:
                return True

            if i < n1 and s1[i] == s3[k]:
                if dfs(i+1,j,k+1):
                    return True

            if j < n2 and s2[j] == s3[k]:
                if dfs(i,j+1,k+1):
                    return True

            return False
            
        return dfs(0,0,0)