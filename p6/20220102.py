n = int(input())
coin = map(int, input().split())
c_max = 0
current = 0
for i in coin:
    current += i
    if current > c_max:
        c_max = current
    elif current < 0:
        current = 0
print(c_max)