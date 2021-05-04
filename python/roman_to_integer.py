# Given a roman numeral, convert it to an integer.

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.


def romanToInt(self, s):
        roman_values = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        i = 0
        final_num = 0
        
        #Iterate through given string
        while i < len(s):
            curr_numeral = s[i]
            #Check if the character before is being subtracted from the one after by checking possible combinations
            if i < len(s) - 1 and ((curr_numeral == "I" and s[i+1] in ["V", "X"]) or (curr_numeral == "X" and s[i+1] in ["L", "C"]) or (curr_numeral == "C" and s[i+1] in ["D", "M"])):
                final_num += (roman_values[s[i+1]] - roman_values[curr_numeral])
                i += 2
            #If it's not...
            else:
                final_num += roman_values[curr_numeral]
                i += 1
        return final_num
