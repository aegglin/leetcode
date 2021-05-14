def intToRoman(self, num: int) -> str:
  
        # This maps the roman numeral values to the values of their digits
        rom_to_dig = { "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
                      "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400,
                      "D": 500, "CM": 900, "M": 1000 }
      
        # This maps the decimal place to the numeric value at that place which then maps
        # to the roman numeral
        rom_by_dec_place = { 0: { "<4": "I", "=4": "IV","<9": "V", "=9": "IX" }, 
                            1: { "<4": "X", "=4": "XL", "<9": "L", "=9": "XC" }, 
                            2: { "<4": "C", "=4": "CD", "<9": "D", "=9": "CM" }, 
                            3: "M" }
        
        rem_num_val = num
        roman_numeral = ""
        # Check what the current greatest decimal place is
        dec_place = len(str(rem_num_val))-1
        
        while rem_num_val > 0:
            new_rom_dig = ""
            curr_digit = int(str(rem_num_val)[0])   
            
            # If the decimal place is 3, then the only option is to put "M"
            if dec_place == 3:
                new_rom_dig = rom_by_dec_place[dec_place]
            # If it's not, then find what the roman numeral should be
            else:
                if curr_digit < 4:
                    new_rom_dig = rom_by_dec_place[dec_place]["<4"]
                elif curr_digit == 4:
                    new_rom_dig = rom_by_dec_place[dec_place]["=4"]
                elif curr_digit < 9:
                    new_rom_dig = rom_by_dec_place[dec_place]["<9"]
                elif curr_digit == 9:
                    new_rom_dig = rom_by_dec_place[dec_place]["=9"]
            
            # Subtract the value of the roman numeral digit just used
            # and add that numeral to the Roman numeral representation
            rem_num_val -= rom_to_dig[new_rom_dig]
            roman_numeral += new_rom_dig
            # Check what the current greatest decimal place is again
            dec_place = len(str(rem_num_val))-1    
            
        return roman_numeral
      
# Explanation:
# The core of the way I did this is noticing the possible combinations of Roman numerals. 
# Ostensibly, there are only seven Roman numerals: I (--> 1), V (--> 5), X (--> 10), L (--> 50), 
# C (--> 100), D (--> 500), M (--> 1000). However, to represent #numbers that contain, 4 or 9 
# e.g. 40, 90, 400, 900, some smaller numerals are placed in front larger ones to indicate 
# that they are being subtracted. These are the rules that apply:
# 
#    I can be placed before V (5) and X (10) to make 4 and 9. 
#    X can be placed before L (50) and C (100) to make 40 and 90. 
#    C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# Thus, these combinations of numerals must also be considered. The rules for determining
# which numeral should be placed are pretty simple, but they vary by decimal place. 
# For example, if trying to represent a 2 in Roman numerals, you have to know if it is
# the first part of 2000, 200, 20, or just 2 itself. As M (1000) is the greatest numeral, if a number
# is greater than that (i.e. the decimal place is 3, or the 1000s place), then at least one
# M must be placed. However, if the decimal place is any other place (100s, 10s, 1s) then 
# the value will vary based on if it's less than 4, equal to 4, greater than 4 but also less 
# than 9, or equal to 9. For all the decimal places besides the 1000s, this rule holds, though
# the numerals themselves are different. The dictionary rom_by_dec_place takes a decimal place
# and maps it to another dictionary, then decides the numeral based on if it is "<4", "=4", 
# "<9", or "=9" as described above. The thousands place always maps to "M". 
