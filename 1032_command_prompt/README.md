```
# BOJ 1032 - Command Prompt

## Problem

[Link to Problem](https://www.acmicpc.net/problem/1032)

You are given `N` filenames, all of which have the same length.  
Your task is to generate a pattern based on these filenames such that:
- If all characters at a certain position are the same across all filenames, that character is kept.
- If any character differs at that position, it is replaced with a question mark (`?`).

## Input

- The first line contains an integer `N` (1 ≤ N ≤ 50), the number of filenames.
- Each of the next `N` lines contains a single filename of the same length (up to 100 characters).

## Output

- A single line containing the resulting pattern.

## Approach

To solve this problem:
1. Read all filenames into a list.
2. For each character index:
   - Compare the characters from all filenames.
   - If they are all the same, keep the character.
   - If not, replace it with `?`.

## Python Code

```python
n = int(input())
filenames = [input() for _ in range(n)]

result = ""

for i in range(len(filenames[0])):
    char = filenames[0][i]
    for j in range(1, n):
        if filenames[j][i] != char:
            char = '?'
            break
    result += char

print(result)
```

## What I learned

- When I first read the problem, I thought it could be solved by comparing each character of the strings.
- To do this, I used nested loops to compare characters at each position.
- Whenever characters differed, I replaced them with a `?` to build the final output string.
- This problem was a good exercise in breaking down a pattern recognition task into simple character comparisons.
- It also helped me appreciate how Python allows concise expressions like list comprehensions.
- The logic itself was simple, but implementing it clearly helped reinforce clean and readable coding practices.
```
