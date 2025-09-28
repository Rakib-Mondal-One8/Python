str = input()

l = 0
r = 0

result = []
ans=""
for c in str:
    ans+=c
    if c == "L":
        l += 1
    else:
        r += 1

    if(l==r):
        result.append(ans)
        ans=""
        l=0
        r=0

print(len(result))
for val in result:
    print(val)