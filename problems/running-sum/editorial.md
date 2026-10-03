# Running Sum of 1d Array: editorial

## Approach

This is the simplest prefix sum. The running sum at index `i` is the running sum at index `i - 1` plus `nums[i]`. Keep a single accumulator and append it after each addition.

The same idea, storing prefix sums so that any range sum becomes a subtraction of two prefixes, is the foundation for the harder problems in this section.

## Complexity

- Time: O(n).
- Space: O(1) beyond the output list.

## Solution

```python
def running_sum(nums: list[int]) -> list[int]:
    result: list[int] = []
    total = 0
    for x in nums:
        total += x
        result.append(total)
    return result
```
