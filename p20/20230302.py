import math

n, t = map(int, input().split())
min_s = 999999
answer = 0
for i in range(n):
    s, d = map(int, input().split())
    if t > s:
        a = math.ceil((t - s) / d) * d - (t - s)
    else:
        a = s - t
    if min_s > a:
        answer = i + 1
        min_s = a
print(answer)
