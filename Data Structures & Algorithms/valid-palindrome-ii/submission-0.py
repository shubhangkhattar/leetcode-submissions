class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s,flag,l,r):            
            while l < r:
                
                if not s[l].isalnum():
                    l += 1
        
                elif not s[r].isalnum():
                    r -= 1
                    
                elif s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                elif flag:
                    return  isPalindrome(s,False,l+1,r) or isPalindrome(s,False,l,r-1)
                else:
                    return False

            return True
        
        return isPalindrome(s,True,0,len(s)-1)
        
        