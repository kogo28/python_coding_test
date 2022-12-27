user_input = int(input())
for i in range(user_input):
    answer = ""
    s = input()
    c = "aeiouAEIOU"
    for j in s:
        if j in c:
            answer += j
    print(answer if len(answer) > 0 else "???")


