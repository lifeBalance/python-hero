# Contains Duplicate: editorial

## Approach

In Python, a set holds each value once. So we just have to traverse the list and add each item to a set:

- If the element is not in the `seen` set, we add it.
- If an element is present in the `seen` set, that's a duplicate, and we can return `True` early.

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

There's an equivalent one-liner:

```python
def contains_duplicate(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)
```

It's very concise and elegant, but it always processes the **whole list**, whereas the loop version returns as soon as the first duplicate appears.

## Complexity

- Time: O(n).
- Space: O(n) for the set.

## Solution

