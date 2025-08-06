# BOJ 1284 – House Numbers

[View on Baekjoon Online Judge](https://www.acmicpc.net/problem/1284)

---

## Problem Description

In digital address plates, each digit has a different width:

- `1` takes **2 units**
- `0` takes **4 units**
- All other digits take **3 units**
- **1 unit of space** is added between each digit
- **2 extra units** are added as margins (1 on each side)

You are given a series of address numbers, and you must calculate the total width of the address plate for each number.  
The program terminates when the input is `"0"`.

---

## Approach

- Read input as a string and iterate over each character.
- Add the corresponding width for each digit.
- Add `(length - 1)` units for the spaces between digits.
- Add 2 units for side margins.

---

## Example

Input:
120
0
Output:
13

Explanation:
- `1` → 2 units  
- `2` → 3 units  
- `0` → 4 units  
- Spaces between digits → 2 units  
- Margins → 2 units  
**Total: 2 + 3 + 4 + 2 + 2 = 13**

---

## What I Learned

- Converting each character in a string to an integer allows simple logic-based calculation.
- It's important to strip newline characters when using `sys.stdin.readline()` to avoid runtime errors.
- Carefully handling spacing and formatting is essential in simulation-style problems.

---

## Final Code (Python)

```python
import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == "0":
        break
    width = 2
    num = list(s)
    for n in num:
        n = int(n)
        if n == 1:
            width += 2
        elif n == 0:
            width += 4
        else:
            width += 3
    width += len(num) - 1
    print(width)

