# leetcode-practice
This repository contains my solutions to various algorithmic problems from LeetCode as well as quantitative models and problems related to finance. My goal is to prepare comprehensively for my Summer 2024 internship in the quantitative finance domain. Each solution is accompanied by my thought process, analysis, and the concepts I employed.

# Array

## Binary Search

[704. Binary Search](https://leetcode.com/problems/binary-search/)

Given an array of integers `nums` which is sorted in ==ascending order==, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Constraints:**

- `1 <= nums.length <= 104`
- `-104 < nums[i], target < 104`
- All the integers in `nums` are **==unique==**.
- `nums` is sorted in ascending order.

```python
while (left < right)
or
while(left <= right)
```

```python
if (nums[middle] > target):
  left = middle 
  or 
  left = middle - 1
```

一般来说==左闭右开== 左闭右闭

左闭右开：

- while (left < right)，这里使用 < ,因为left == right在区间[left, right)是没有意义的
- if (nums[middle] > target) right 更新为 middle，因为当前nums[middle]不等于target，去左区间继续寻找，而寻找区间是左闭右开区间，所以right更新为middle，即：下一个查询区间不会去比较nums[middle]

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  

        while left < right:  
            middle = left + (right - left) // 2
            # middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle  
            else:
                return middle
        return -1 
```

[35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

Consider the out the `nums` range: 0 and `len(nums)`
Also, when the while ended, left > right
return left or right + 1

```python
        if (nums[0] > target):
            return 0
        if (nums[-1] < target):
            return len(nums)
```



[34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

==寻找边界== 上面三个题的通解

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target + 1) - 1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]
```

[69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)

```python
        if (x < 1000000):
            for i in range(1000):
                if i * i <= x and (i + 1) * (i + 1) > x:
                    return i
```

但通解最好别用这个。

[367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)

```python
        left, right = 1, num // 2
        if num == 1 or num == 4:
            return True
```

## Remove Element

[27. Remove Element](https://leetcode.com/problems/remove-element/)

### 双指针法

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        size = len(nums)
        while fast < size:
            # slow 用来收集不等于 val 的值，
            # 如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
```

[26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

差序对比

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        while (fast < len(nums)):
            if (nums[fast] != nums[slow]):
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1
```

[283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        fast = 0
        while (fast < len(nums)):
            if (nums[fast] != 0):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
```

[844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def newString(str):
            fast = 0
            result = []
            while (fast < len(str)):
                if (str[fast] == '#'):
                    result = result[:-1]
                else:
                    result += [str[fast]]
                fast += 1
            return result
        return newString(s) == newString(t)
      
```

## Squares of a Sorted Array

[977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

因为最后排序的是平方 所以前后俩指针

```python
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
```









