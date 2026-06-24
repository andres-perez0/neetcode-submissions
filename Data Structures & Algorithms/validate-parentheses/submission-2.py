class Solution:
    def isValid(self, s: str) -> bool: 
        opening = []
        
        for c in s:
            if c == "(" or c == "{" or c == "[":
                opening.append(c)
            
            if c == ")" or c == "}" or c == "]":
                if len(opening) == 0:
                    return False

                op = opening.pop()
                if c == ")" and op != "(":
                    return False
                if c == "}" and op != "{":
                    return False
                if c == "]" and op != "[":
                    return False
                    
        if len(opening) != 0:
            return False

        return True