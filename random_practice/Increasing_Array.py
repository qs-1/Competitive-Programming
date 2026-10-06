n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(0)
else:
    moves = 0
    prev = arr[0]
    for num in arr[1:]:
        if num<prev:
            # print(prev,num,prev-num)
            moves += prev-num
        else:
            prev = num
    print(moves)