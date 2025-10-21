def make_zigzag(n, num):
    ans = 0
    # We only need to handle even indices as per your logic
    for i in range(n):
        if i % 2 == 0:
            # check left neighbor only if it exists
            if i - 1 >= 0 and num[i - 1] <= num[i]:
                ans += (num[i] - num[i - 1]) + 1
                num[i] = num[i - 1] - 1

            # check right neighbor only if it exists (bounds first!)
            if i + 1 < n and num[i + 1] <= num[i]:
                num[i + 1] = num[i] + 1
                ans += 1

    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().strip().split()))   # use split() because numbers are space-separated
    print(make_zigzag(n, s))
