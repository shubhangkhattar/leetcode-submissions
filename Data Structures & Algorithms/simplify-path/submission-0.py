class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path += "/"
        stack = []
        curr = ""

        for char in path:
            if char == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "." and curr != "":
                    stack.append(curr)
                curr = ""    
            else:
                curr += char
                
        print(stack)
        return "/" + "/".join(stack)
                
                    
                
            
