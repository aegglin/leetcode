# Given n pairs of parentheses, write a function to generate 
# all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        final_list = []
        curr_str = '('
        self.generate_recursion(n, n-1, n, curr_str, final_list)
        
        return final_list
    
    def generate_recursion(self, n: int, num_left_parens: int, num_right_parens: int, curr_str: str, final_list: List[str]) -> str:
        if num_left_parens > num_right_parens:
            return None
        if len(curr_str) == n*2 and num_left_parens == num_right_parens:
            final_list.append(curr_str)
            return final_list
        else:
            
            if num_left_parens > 0:
                self.generate_recursion(n, num_left_parens-1, num_right_parens, curr_str+"(", final_list)
            if num_right_parens > 0:
                self.generate_recursion(n, num_left_parens, num_right_parens-1, curr_str+")",  final_list)

            return final_list
            
