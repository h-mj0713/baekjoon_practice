# BOJ 1009 – Data Processing

[View Problem on Baekjoon](https://www.acmicpc.net/problem/1009)

## Problem Summary

Given two integers `a` and `b`, compute the last digit of `a^b`.  
However, if the result ends with 0, print **10** instead of 0.

---

## My Initial Approach

At first, I submitted a simple and intuitive solution using `a ** b % 10`.  
However, this approach caused a **Time Limit Exceeded (TLE)** error on large inputs because:

- Calculating `a ** b` directly is too slow when `b` is large (up to 1 billion).
- The result could become a huge number, leading to performance issues.

So I needed a way to **reduce the size of the numbers** being processed without changing the result.

---

## Final Idea Using Patterns

I observed that the **last digit** of `a^b` follows a **repeating cycle** depending on the value of `a % 10`.

For example, when `a = 2`, the last digits of its powers repeat every 4 steps:


By storing these cycles in a dictionary, I was able to avoid calculating large powers and instead use simple modular indexing to get the correct answer efficiently.

---

## What I Learned

- Brute-force power calculation is not practical with large exponents.
- Many power problems can be solved by recognizing **cyclic patterns** in remainders.
- Dictionaries are a great way to map fixed patterns for fast lookup.
- `(b - 1) % len(cycle)` gives the correct 0-based index into the pattern.

---

## Final Code (Python)

```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a %= 10

    if a == 0:
        print(10)
    else:
        pattern = {
            1: [1],
            2: [2, 4, 8, 6],
            3: [3, 9, 7, 1],
            4: [4, 6],
            5: [5],
            6: [6],
            7: [7, 9, 3, 1],
            8: [8, 4, 2, 6],
            9: [9, 1]
        }

        cycle = pattern[a]
        index = (b - 1) % len(cycle)
        print(cycle[index])
