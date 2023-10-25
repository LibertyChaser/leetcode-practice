class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        front = 0
        back = len(nums) - 1
        result = []
        while (front <= back):
            if (nums[front] ** 2 < nums[back] ** 2):
                result += [nums[back] ** 2]
                back -= 1
            else:
                result += [nums[front] ** 2]
                front += 1
            
        return result[::-1]
