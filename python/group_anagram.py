# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        final_list_inds = {}
        
        i = 0
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word not in final_list_inds:
                final_list_inds[sorted_word] = i
                
                if i >= len(final_list):
                    final_list.append([word])
                
                i += 1
            else:
                final_list[final_list_inds[sorted_word]].append(word)
                
        return final_list
