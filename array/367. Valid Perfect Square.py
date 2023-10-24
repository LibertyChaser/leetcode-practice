class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num // 2
        if num == 1 or num == 4:
            return True
        while (left < right):
            middle = left + (right - left) // 2
            if (middle * middle < num):
                left = middle + 1
            elif (middle * middle > num):
                right = middle
            else:
                return True
        return False