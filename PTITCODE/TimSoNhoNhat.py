 # Nhap du lieu dau vao i
t = int(input())
while t > 0:
    t -= 1
    s, i, ans, tmp = input(), 0, 99999999, -1
    while i < len(s):
        tmp = -1
        if (s[i].isdigit()):
            tmp = 0
        while (i < len(s) and s[i].isdigit()):
            tmp = tmp * 10 + int(i)
            i += 1
        if tmp != -1:
            ans = min(ans, tmp)
        i += 1
    if tmp != -1:
        ans = min(ans,tmp)
    print(ans)


