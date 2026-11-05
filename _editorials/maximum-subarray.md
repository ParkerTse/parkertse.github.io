---
title: Maximum Subarray
number: 53
difficulty: Medium
tags: [array, dynamic programming]
date: 2026-11-04
link: https://leetcode.com/problems/maximum-subarray/
---

## Problem

Given an integer array `nums`, find the subarray with the maximum sum, and return its sum.

## Example

**Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]
**Output:** 6
**Explanation:** The subarray [4,-1,2,1] has the largest sum 6.

## Intuition

My first intuition was to find the most negative subarray on the left and right and remove them. However, there is a better approach where you only need to loop through the array once.

Because we are only looping through the array once, there are only two options to decide from:
A. Add the number to our existing subarray **or** B. Reset the subarray so our number is the first element of a new subarray.

This leaves us with 1 essential question: How do we decide between A or B?

Things to think about before reading the approach:

1. Break it up into cases. What should we do when our subarray's total is negative, and what happens when its positive?
2. Which variables do we need?

## Approach

1. Create a variable to store the max value of our subarray and initialize it to the first element of the array.
2. Create a variable to store the total value of our subarray and initialize it to 0.
3. Loop through the array.
   -If the total positive, add the element to the subarray.
   -If the total is negative, it is always better to start a new array.
   -If you can't see this, then break it into cases: What happens when element is positive and what happens when it's negative. Positive: Great! Our element X is always greater than negative number + x. Negative: Also good! Adding two negatives makes an even bigger negative so its better to just start with our negative element X.
   -Check whether our current subarray sum is greater than the max value variable.
4. Return max value variable

## Complexity

- **Time Complexity:** $\mathcal{O}(n)$ — We loop through the array once.
- **Space Complexity:** $\mathcal{O}(1)$ — We don't need an extra array, just two variables.

## Code

```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        total = 0
        for num in nums:
            # if total is positive, then add to the subarray
            if total > 0:
                total += num
            # if the total is negative, it is better to start at the current element
            else:
                total = num

            if total > max_sum:
                max_sum = total

        return max_sum

```
