# Implement the myAtoi(string s) function, which converts a 
# string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

    # 1.) Read in and ignore any leading whitespace.
    # 
    # 2.) Check if the next character (if not already at the end of the string) is '-' or '+'.
    # Read this character in if it is either. This determines if the final result is negative or positive respectively. 
    # Assume the result is positive if neither is present.
    # 
    # 3.) Read in next the characters until the next non-digit charcter or the end of the input is reached. 
    # The rest of the string is ignored.
    #
    # 4.) Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
    # If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    #
    # 5.) If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
    # then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, 
    # and integers greater than 231 - 1 should be clamped to 231 - 1.
    #
    # 6.) Return the integer as the final result.

def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        
        if len(s) == 0:
            return 0
        
        int_sign = 1
        
        if s[0] == '-':
            int_sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        i = 0
        curr_str = ""
        while i < len(s) and s[i].isdigit():
            curr_str += s[i]
            i += 1
        if len(curr_str) > 0:
            converted_int = int(curr_str)
            converted_int *= int_sign
        
            if converted_int < -2**31:
                converted_int = (-2**31)
            elif converted_int > ((2**31) - 1):
                converted_int = ((2**31)-1)
        return converted_int if len(curr_str) > 0 else 0
