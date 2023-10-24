class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLeftIndex(x):
            left, right = 0, len(nums)
            while left < right:
                middle = left + (right - left) // 2
                if nums[middle] < x:
                    left = middle + 1
                else:
                    right = middle
            return left

        left = searchLeftIndex(target)
        right = searchLeftIndex(target + 1) - 1

        if left <= right:
            return [left, right]

        return [-1, -1]