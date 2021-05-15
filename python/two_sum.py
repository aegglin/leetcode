def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute Force approach O(n^2) time complexity
        # as for each element, we find its complement by looking through
        # the rest of the list, which takes O(n) time
        for i, x in enumerate(nums):
            other_nums = nums[i+1:]
            for other_index, other_num in enumerate(other_nums):
               if x + other_num == target:
                    return [i, other_index + (len(nums)-len(other_nums))]
        
        
        # Two-pass Hash Table
        # This reduces the time for each lookup to O(1)
         nums_indices = defaultdict(list) #Using a default dictionary to allow a list comprehension to fill in each value
           
        # O(n) for first run to get indices from numbers in list
         [ nums_indices[num].append(i) for i, num in enumerate(nums) ]
        # O(n) again to iterate through again and if their complement exists
         for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_indices:
                if complement != num:
                    return [ i, nums_indices[complement].pop() ]
                elif len(nums_indices[complement]) > 1:
                    return [ nums_indices[complement].pop(), nums_indices[complement].pop() ]
              
            
        # One-pass Hash table
        # You don't need two passes to go through the table
        # and also check if a complement exists
        nums_indices = {} # regular dict this time because it won't be filled beforehand so we don't have to worry about duplicates
        # O(n) because we just require one traversal
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_indices:
                return [ nums_indices[complement], i ]
            nums_indices[num] = i
