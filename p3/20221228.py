n = int(input())
l = []
for i in range(n):
    s, e = input().split()
    s = s.split("/")
    s = int(s[0])*100 + int(s[1])
    e = e.split("/")
    e = int(e[0]) * 100 + int(e[1])
    l.append([s, e])
l.sort(key=lambda x: (x[0], -x[1]))
answer = "Yes"
a = l[-1][1]
for i in l[-2::-1]:
    if i[1] < a:
        answer = "No"
        break
    a = max(a, i[1])
print(answer)