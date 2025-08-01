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
