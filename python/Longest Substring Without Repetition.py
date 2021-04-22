class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letters = {}
        longest_str = ""
        curr_str = ""
        
        #Iterate through the entire string
        for i, letter in enumerate(s):
            #if you haven't seen the letter yet, add to dict and keep going
            if not letter in letters:
                letters[letter] = True
                curr_str += letter
            
            #if the letter is a duplicate
            else:
                if len(curr_str) > len(longest_str):
                    longest_str = curr_str
                    
                #reset the dictionary
                letters = {}
                
                #Find the first character after the first instance of the duplicate
                #and start the string over from there
                first_repeat_ind = s.rfind(letter, i-len(curr_str),i)
                curr_str = s[first_repeat_ind+1:i+1]
                for curr_letter in curr_str:
                    letters[curr_letter] = True
                
            #Check for longest string at the end (i.e. without repeating)
        if len(curr_str) > len(longest_str):
            longest_str = curr_str
        return len(longest_str)
        
            
