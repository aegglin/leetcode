#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first_str = strs[0]
        max_common_str = first_str
        for i in range(1, len(strs)):
            curr_str = strs[i]
            curr_common_str = ""
            j = 0
            while j < len(curr_str) and j < len(first_str) and curr_str[j] == first_str[j]:
                curr_common_str += curr_str[j]
                j += 1
            if len(curr_common_str) < len(max_common_str):
                max_common_str = curr_common_str
        return max_common_str
