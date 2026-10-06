cases = int(input())
for _ in range(cases):
    s = input()
    n = len(s)

    if n == 1:
        print(0)
        continue

    rightmost_nonzero = None
    for i in range(n-1, -1, -1):
        if s[i] != '0':
            rightmost_nonzero = i
            break
    
    # remove all non zeros from the right
    # to get best 0000n form and cost = 1

    leftmost_nonzeros = 0
    for i in range(rightmost_nonzero):
        if s[i] != '0':
            leftmost_nonzeros += 1
    
    print(leftmost_nonzeros + n-rightmost_nonzero-1)



