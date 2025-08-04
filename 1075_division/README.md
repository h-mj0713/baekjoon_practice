# BOJ 1075 - Division

## Problem Summary

Given an integer `N` (N ≥ 100) and another integer `F` (1 ≤ F ≤ 100),  
replace the last two digits of `N` with `'00'`.  
Find the **smallest non-negative number** you can add to this new value such that it becomes divisible by `F`.

Print the last two digits of that number as a two-digit string (e.g., `03`, `45`, `70`).

---

## Example

### Input
```
275
5
```

### Output
```
00
```

### Explanation
Replace last two digits of 275 → 200  
Check values from 200 to 299  
200 is divisible by 5 → answer is `00`

---

## Solution Idea

- Cut off the last two digits of `N` using integer division and multiplication:
  ```python
  new_num = (N // 100) * 100
  ```
- Try adding values from 0 to 99.
- The first value where `(new_num + i) % F == 0` is the answer.
- Format the output using `f"{i:02d}"` to ensure two-digit result.

---

## Final Code (Python)

```python
import sys
input = sys.stdin.readline

num = int(input())
f = int(input())

new_num = (num // 100) * 100
change = 0

while True:
    if new_num % f == 0:
        print(f"{change:02d}")
        break
    new_num += 1
    change += 1
    
```

---

## What I Learned

- How to truncate the last two digits of a number using `(num // 100) * 100`.
- How to format integers with leading zeros using `f"{i:02d}"`.
- Brute-force can be efficient when the range is small (0–99).
