def sort012(a):
    n = len(a)
    c1 = 0
    c2 = 0
    c0 = 0
    ans = []
    for i in a:
        if i == 0:
            c0 += 1
        if i == 1:
            c1 += 1
        if i == 2:
            c2 += 1
    for i in range(c0):
        ans.append(0)
    for i in range(c1):
        ans.append(1)
    for i in range(c2):
        ans.append(2)
    return ans


N = int(input())
arr = list(map(int, input().split()))

sorted_arr = sort012(arr)
for i in sorted_arr:
    print(i, end=' ')
