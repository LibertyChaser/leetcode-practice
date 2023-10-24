class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while (left < right):
            middle = left + (right - left) // 2
            if (nums[middle] > target):
                right = middle
            elif (nums[middle] < target):
                left = middle + 1
            else:
                return middle
        return -1