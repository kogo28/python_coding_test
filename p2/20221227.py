# import math
#
# n = math.ceil(10**4.5)
# prime_n = set(range(2, n+1))
#
# for i in range(4, n+1):
#     for j in range(2, math.ceil(i**0.5)+1):
#         if i % j == 0:
#             prime_n.remove(i)
#             break
# prime_n = sorted(list(prime_n))
# # print(prime_n) 소수리스트 확인
#
# d = dict()
# a, b = map(int, input().split())
# if b < a:
#     a, b = b, a
# if a < 2: a = 2
# if b > 10**9: b = 10**9
# for i in range(a, b+1):
#     if i < 4:
#         d[i] = d.get(i, 0) + 1
#         continue
#     for j in prime_n:
#         if j > math.ceil(i**0.5):
#             break
#         if i % j == 0:
#             d[j] = d.get(j, 0) + 1
#             d[i // j] = d.get(i // j, 0) + 1
#     d[i] = d.get(i, 0) + 1
# answer = sorted(d.items(), key= lambda item : (item[1], -item[0]), reverse=True)
# print(answer[0][0])
# 시간초과

a, b = map(int, input().split())
answer = 2
if a == b:
    for i in range(2, int(a**0.5)+2):
        if a % i == 0:
            answer = i
            break
    else:
        answer = a
print(answer)