class Solution:
    def mySqrt(self, x: int) -> int:
        if (x < 1000000):
            for i in range(1000):
                if i * i <= x and (i + 1) * (i + 1) > x:
                    return i
        
        left, right = 100, x // 100
        while(left < right):
            middle = left + (right - left) // 2
            if (middle * middle < x):
                left = middle + 1
            elif (middle * middle > x):
                right = middle
            else:
                return middle
        return left - 1
    
        # This doesn't work since it will except the the answer. The answer requires the floor version of the number. Just use the traditional one.
        #     while(left < right):
        #         middle = left + (right - left) // 2
        #     if (middle * middle < x):
        #         left = middle + 1
        #     else:
        #         right = middle
        # return left
