# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
testCases = int(input())
for _ in range(testCases):
    numbers = int(input())
    arr = list(map(int, input().split(' ')))
    cost = 0
    for i in range(numbers-1):
        _min = arr[i]
        _minIndex = i
        for j in range(i, numbers):
            if _min > arr[j]:
                _min = arr[j]
                _minIndex = j
        cost += _minIndex - i + 1
        arr[i:_minIndex+1] = arr[i:_minIndex+1][::-1]
    print(f'Case #{_+1}: {cost}')
