---
title: Merge Intervals
number: 56
difficulty: Medium
tags: [array, sorting]
date: 2026-11-05
link: https://leetcode.com/problems/merge-intervals/
---

## Problem

Given an integer array `intervals`, merge all the overlapping intervals.

## Example

**Input:** intervals = [[1,3],[2,6],[8,10],[15,18]]
**Output:** [[1,6],[8,10],[15,18]]
**Explanation:** Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

## Intuition

The brute force way would be to loop through the intervals array and checking if any interval merges with any of the exisitng intervals in your resulting array. This would result in an $\mathcal{O}(n^2)$ runtime since for every element, we need to loop through our resulting array. Is there a better approach where we only need to add to the resulting array and not scan the whole thing?

If you think about a number line, our initial intervals array has a bunch of scattered intervals. How can iterate through the intervals array without jumping back and forth?

We can sort the intervals array based on the starting point. This way, when we iterate we know that specific interval is the closest possible to the ending interval in our resulting array. From there, we can decide whether or not to add it or create a new interval.

Whenn adding to the array, we have to be careful in changing the interval. There are two cases:

1. The interval is a subset of the existing interval
2. The interval extends the existing interval

## Approach

1. Create an array to store your result.
2. Sort the intervals array by start point.
3. Loop through the intervals array.
   - If the starting point is outside the range of the existing array, add it to the array.
   - If the starting points is within the range there are two cases:
     - a. It is a subset
     - b. It extends the range
4. Return your result array.

## Complexity

- **Time Complexity:** $\mathcal{O}(nlogn)$ — Sorting takes $\mathcal{O}(nlogn)$ and looping through intervals takes $\mathcal{O}(n)$, so $\mathcal{O}(nlogn)$ dominates.
- **Space Complexity:** $\mathcal{O}(n)$ — Since we need to create a resulting array.

## Code

```python
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            # if the start of the interval is greater than the end of the last interval, then it cannot merge
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            # if it can merge, check if the interval is a subset of the interval, or if it extends the interval
            else:
                if res[-1][1] < interval[1]:
                    res[-1][1] = interval[1]

        return res

```
