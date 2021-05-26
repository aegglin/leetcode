# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
# 
# An input string is valid if:
#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.

def isValid(self, s: str) -> bool:
        parens = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                parens.append(char)
            else:
                if len(parens) > 0: 
                    curr_opening_paren = parens.pop()
                    if (char == ")" and curr_opening_paren == "(") or \
                        (char == "]" and curr_opening_paren == "[" or \
                        (char == "}" and curr_opening_paren == "{")):
                        continue
                    
                return False
        
        return True if len(parens) == 0 else False
