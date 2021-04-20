class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i, x in enumerate(nums):
            other_nums = nums[i+1:]
            for other_index, other_num in enumerate(other_nums):
                if x + other_num == target:
                    return [i, other_index + (len(nums)-len(other_nums))]
