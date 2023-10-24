# leetcode-practice
This repository contains my solutions to various algorithmic problems from LeetCode as well as quantitative models and problems related to finance. My goal is to prepare comprehensively for my Summer 2024 internship in the quantitative finance domain. Each solution is accompanied by my thought process, analysis, and the concepts I employed.

# Array

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



[367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)

```python
        left, right = 1, num // 2
        if num == 1 or num == 4:
            return True
```



```python
Class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) == 0):
            return [-1, -1]
        left, right = 0, len(nums)

        while (left < right):
            middle = left + (right - left) // 2
            if (nums[middle] > target):
                right = middle
            elif(nums[middle] < target):
                left = middle + 1
            else:
                break;

        if (left >= right):
            return [-1, -1]

        pre_middle = middle
        pre_left = left
        pre_right = right

        if (nums[0] == target):
            left_ind = 0
        else:
            left, right = pre_left, pre_middle
            while (left <= right):
                if (nums[left] == target and nums[left - 1] != target):
                    break
                middle = left + (right - left) // 2
                if (nums[middle] < target):
                    left = middle
                else:
                    right = middle

            left_ind = left

        if (nums[-1] == target):
            right_ind = len(nums)
        else:
            left, right = pre_middle, pre_right
            while (left <= right):
                if (nums[left] == target and nums[left + 1] != target):
                    break
                middle = left + (right - left) // 2
                if (nums[middle] > target):
                    right = middle
                else:
                    left = middle
            
            right_ind = left

        return [left_ind, right_ind]
```



