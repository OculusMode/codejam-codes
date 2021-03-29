# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7
# ReverSort Engineering
# I have a hunch that we can combine 2 loops in one, but didn't have time to complete. The timecomplexity will be O(n) instead of O(2n) after that.
testCases = int(input())
for _ in range(testCases):
    n, cost = list(map(int, input().split(' ')))
    # minimum cost will be n, and maximum will be n + n-1 + n-2 + ... + 2 => n(n+1)/2 - 1
    if cost < n - 1 or cost > n*(n+1)/2 - 1:
        print(f'Case #{_+1}: IMPOSSIBLE')
    else:
        arr = []
        arr = []
        myArr = list(range(1, n+1))
        for i in range(n-1):
            remaining = n - 2 - i
            if cost - remaining <= n - i:
                maxCost = cost-remaining
                cost -= maxCost
            else:
                maxCost = n-i
                cost-=maxCost
            arr.append(maxCost)
        arr.reverse()
        for i in range(n-1):
            if arr[i]!=1:
                myArr[n-i-2:n-i-2+arr[i]] = myArr[n-i-2:n-i-2+arr[i]][::-1]
        print(f'Case #{_+1}: {" ".join(map(str, myArr))}')
