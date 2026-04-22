class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []

        def isPalindrom(left,right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left,right = left+1,right-1
            return True
        
        def dfs(i,curr_list):
            if i == len(s):
                result.append(curr_list[:])
                return
            
            for j in range(i,len(s)):
                if isPalindrom(i,j):
                    curr_list.append(s[i:j+1])
                    dfs(j+1,curr_list)
                    curr_list.pop()
        
        dfs(0,[])
        return result





