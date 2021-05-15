# This problem is similar to the problem in two_sum.py but, unlike that problem, the input array is sorted. 

def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # O(n) for time complexity because of the loop
        # O(1) for space complexity as we don't have any data structures
        
        head_index = 0
        tail_index = len(numbers)-1
        
        index_sum = numbers[head_index] + numbers[tail_index]
        
        while index_sum != target:
            if index_sum > target:
                tail_index -= 1
            elif index_sum < target:
                head_index += 1
            index_sum = numbers[head_index] + numbers[tail_index]
        return [ head_index+1, tail_index+1 ]
      
      
# Explanation: We use the following algorithm -- only keep track of two variables,
# a low(head) index and high(tail) index. These variables are initialized as the first and last 
# indices of the list provided. We then iteratively check if the sum of the elements at
# these two indices is equal to the target. If it is, then we're done. If it's not, there
# are two options. If the sum is greater than the target, we move the tail index back one
# which decreases its value. If the sum is less than the target, we move the head variable
# up one, which increases its value. We do this until the sum is equal to the target. 
# In this way, we slowly narrow the searching area from both directions while not having to make 
# use of a data structure to increase the space complexity. 
