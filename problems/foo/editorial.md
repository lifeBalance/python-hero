# Hello world 2: editorial

## Approach

The point of this exercise is to understand that functions can return values, e.g. strings, numbers, etc.

> [!NOTE]
> Note that function **can** return values, but don't have to; for example, the previous version of our `Hello world!` problem didn't return any value at all, it simply printed it to the console.

So remember returning and printing are not the same thing, even if we're dealing with the same value:

- The `print`function writes to the console and returns back `None`.
- The `return` statement returns a value to whoever called the function.

The tests call your function and look at what comes back, so a solution that only prints returns nothing.

> [!NOTE]
> In programming, we have to be very careful with little details like capitalization, commas, spaces, etc. The string `"Hello, world!"` has a capital `H`, a comma, a space and an exclamation mark. So `"Hello World"` is not the same string!

## Complexity

- Time: O(1).
- Space: O(1).

## Solution

```python
def hello_world_2() -> str:
    return "Hello, world!"
```