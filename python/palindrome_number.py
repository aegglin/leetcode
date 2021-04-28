#Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. 
#For example, 121 is palindrome while 123 is not.

def isPalindrome(self, x):
        #using str conversion:
        #return str(x) == str(x)[::-1]
  
        #without converting to a string: 
        x_num = x
        curr_num = 0  
        while x_num > 0:  
            last_digit = x_num % 10  
            curr_num = curr_num * 10 + last_digit
            x_num //= 10  
        return curr_num == x
      
 
