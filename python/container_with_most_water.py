class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            curr_width = right - left
            curr_height = height[left] if height[left] < height[right] else height[right]
            curr_area = curr_width * curr_height
            
            if curr_area > max_area:
                max_area = curr_area
            
            if curr_height == height[left]:
                left += 1
            elif curr_height == height[right]:
                right -= 1
            
        return max_area
