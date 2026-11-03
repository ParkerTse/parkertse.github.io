---
# Copy this file to _editorials/<slug>.md (e.g. two-sum.md); the filename becomes the URL.
# Files starting with "_" are never published.
title: Two Sum
number: 1
difficulty: Easy          # Easy | Medium | Hard
tags: [array, hash map]
date: 2026-11-03
link: https://leetcode.com/problems/two-sum/
---

## Problem

One or two sentences restating the problem in your own words.

## Intuition

What's the key observation? Why does the naive approach fall short?

## Approach

1. Step one.
2. Step two.

## Complexity

- Time: $O(n)$
- Space: $O(n)$

Display math works too:

$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$

## Code

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], i]
            seen[x] = i
```

## Edge cases

- Duplicates, negatives, empty input, etc.
