# BOJ 1010 – Bridge Construction

[View problem on Baekjoon](https://www.acmicpc.net/problem/1010)

### Problem
You have N sites on the west and M on the east.
You need to connect N bridges without crossing.

### Solution
So I implemented a simple combination function using factorials.
This works fine since inputs are small (max 30).

## What I Thought AND Learned

When I saw the condition that bridges must not cross,  
I immediately thought this was a combination problem.  
I couldn’t recall the exact formula for combinations at the moment,  
so I implemented it manually using a factorial function.

The problem itself was simple,  
but it was a meaningful experience to recognize a real-world scenario where combinations apply and to actually implement it from scratch.

```python(first)
def factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    print(combination(M, N))


# Alternative: using math.comb (Python 3.8+)
# This version is more concise and doesn't require a manual factorial function.

import math

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(math.comb(M, N))
