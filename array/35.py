class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        if (nums[0] > target):
            return 0
        if (nums[-1] < target):
            return len(nums)
        while (left < right):
            middle = left + (right - left) // 2
            if (nums[middle] < target):
                left = middle + 1
            else:
                right = middle  
        return left