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
        