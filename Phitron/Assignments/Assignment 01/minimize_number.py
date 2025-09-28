n = int(input())
a = list(map(int,input().split()))

ans = 1e9
for val in a:
    cnt = 0
    while(val%2 == 0):
        val//=2
        cnt+=1
    ans = min(ans,cnt)

print(ans)