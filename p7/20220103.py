n, m = map(int, input().split())
l = list(map(int, input().split()))
l2 = [0]
for i in range(n):
    l2.append(l2[i] + l[i])
for i in range(m):
    a, b = map(int, input().split())
    answer = l2[b] - l2[a - 1]
    print(answer if answer <= 0 else "+" + str(answer))