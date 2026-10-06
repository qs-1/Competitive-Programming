cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input()

    for i in range(n):
        if s[i] == 'A':
            break
        
    for j in range(n-1,-1,-1):
        if s[j] == 'B':
            break
    # if the first A is after the last B then cant swap
    if j<i:
        print(0)
    else:
        print(j-i)