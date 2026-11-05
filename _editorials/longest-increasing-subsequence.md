---
title: Longest Increasing Subsequence
number: 300
difficulty: Medium
tags: [array, binary search, dynamic programming]
date: 2026-11-03
link: https://leetcode.com/problems/longest-increasing-subsequence/
---

## Problem

Given an integer array `nums`, return the length of the longest strictly increasing subsequence. The sequence does not need to be contiguous.

## Example

**Input:** `nums = [10, 9, 2, 5, 3, 7, 101, 18]`  
**Output:** `4`  
**Explanation:** The longest increasing subsequence is `[2, 3, 7, 101]` (or `[2, 3, 7, 18]`), so the length is 4.

## Intuition

First think about:
1. How can we store every single subsequence?
2. Do we need to store every single subsequence?
3. When processing a new number, do we need to rebuild our previous sequences?

If we loop through `[10, 9, 2, 5, 3, 7, 101, 18]`, we start with `10`. When we encounter `9`, we cannot extend `[10]` because $9 < 10$. However, `9` is a better starting candidate than `10` because it gives us a wider range of future numbers that can build an increasing sequence. The same applies when we see `2`—we replace `9` with `2`.

When `5` arrives, since $5 > 2$, we can extend our sequence to `[2, 5]`. Next, `3` arrives. Since $3 < 5$, we replace `5` with `3`, giving us `[2, 3]`. Lowering the tail value from 5 to 3 makes it easier for future numbers to extend the sequence.

What about elements appearing later that are smaller than earlier ones?
Consider `nums = [10, 9, 2, 5, 3, 1, 7, 101, 18]`. At `1`, our active tails array is `[2, 3]`. Even though `1` comes after `2`, replacing `2` with `1` gives us `[1, 3]`. 

Overwriting an element does **not** shrink the size of our array, so our recorded maximum length is never lost. Instead, it creates a new subsequence starting at `1` that can take advantage of future elements while preserving the length we achieved so far.

Things to think about before reading the approach:
1. How are we going to replace elements in the array? Hint: The array is sorted.
2. Do we need to store the whole sequence, or do we only care about where it ends?

## Approach

1. Initialize an empty array `tails` to store the smallest ending values for all sequence lengths found so far.
2. For each number `num` in `nums`:
   - If `tails` is empty or `num` is strictly greater than `tails[-1]`, append `num` to `tails`.
   - Otherwise, use binary search (`bisect_left`) to find the first index `idx` where `tails[idx] >= num`, and set `tails[idx] = num`.
3. Return `len(tails)`.

## Complexity

- **Time Complexity:** $\mathcal{O}(n \log n)$ — We process $n$ elements, performing a binary search of size at most $n$ ($\mathcal{O}(\log n)$) for each.
- **Space Complexity:** $\mathcal{O}(n)$ — The `tails` array requires up to $n$ space in the worst case.

## Code

```python
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []
        for num in nums:
            # If num is greater than all tails, extend the longest sequence
            if not tails or num > tails[-1]:
                tails.append(num)
            else:
                # Find the first element >= num and replace it with a smaller tail
                idx = bisect_left(tails, num)
                tails[idx] = num
                
        return len(tails)
