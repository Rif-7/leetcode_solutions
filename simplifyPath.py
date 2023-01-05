class Solution:
    def simplifyPath(self, path: str) -> str:
        res = ""
        folders = path.split("/")
        stack = []
        for f in folders:
            if not f or f == ".":
                continue
                
            elif f == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(f)
        
        for f in stack:
            res += "/" + f
        
        return res if res else "/"
            
        