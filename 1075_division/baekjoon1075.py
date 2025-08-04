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
    