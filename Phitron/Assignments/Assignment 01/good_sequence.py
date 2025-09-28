n = int(input())
a = list(map(int, input().split()))
dist = set(a)

ans = 0
for val in dist:
    x = a.count(val)
    if x < val:
        ans += x
    if x >= val:
        ans += x - val

print(ans)
