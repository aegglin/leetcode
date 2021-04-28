# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        new_str = ""
        has_sign = False
        for digit in str(x):
            if digit == "-":
                has_sign = True
            else:
                new_str = digit + new_str
    
        if has_sign:
            new_str = "-" + new_str
        new_int = int(new_str)
        if new_int < -2**31 or new_int > (2**31)-1:
            return 0
        
        return new_int
