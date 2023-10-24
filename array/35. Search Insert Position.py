class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)
        
        # Special Cases
        if (nums[0] > target):
            return 0
        if (nums[-1] < target):
            return len(nums)
        
        while (left < right):
            middle = left + (right - left) // 2
            # find the left index
            if (nums[middle] < target):
                left = middle + 1
            else:
                right = middle  
                
        return left