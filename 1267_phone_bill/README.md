# BOJ 1267 – Phone Bill

[View problem on Baekjoon](https://www.acmicpc.net/problem/1267)

## Problem Summary

There are two billing systems:
- **Yongsik (Y plan):** 10 won every 30 seconds
- **Minsik (M plan):** 15 won every 60 seconds

You're given a list of call durations. Calculate the total cost for both plans and output the cheaper one. If costs are the same, print both.

## Solution

- Use integer division to count how many chunks each call falls into.
- Multiply by the unit price.
- Accumulate the total for each plan and compare.

## What I Learned

- Simple math with integer division is enough to simulate pricing models.
- Use `//` to divide and add 1 to cover all ranges (even 0~29 sec counts as one unit).
- This was a good practice in applying basic simulation logic.

## Final Code (Python)

```python
import sys
input = sys.stdin.readline

n = int(input())
call_times = list(map(int, input().split()))

youngsik_total = 0
minsik_total = 0

for time in call_times:
    youngsik_total += ((time // 30) + 1) * 10
    minsik_total += ((time // 60) + 1) * 15

if youngsik_total < minsik_total:
    print("Y", youngsik_total)
elif youngsik_total > minsik_total:
    print("M", minsik_total)
else:
    print("Y M", youngsik_total)
