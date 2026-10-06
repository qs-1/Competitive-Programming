n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))
rdiffsum = [0]*n
ldiffsum = [0]*n

for i in range(1,n):
    rdiffsum[i] = rdiffsum[i-1] + max(0, arr[i-1] - arr[i])
    ldiffsum[n-i-1] = ldiffsum[n-i] + max(0, arr[n-i] - arr[n-i-1])

for _ in range(m):
    s,t = list(map(int, input().split()))
    if s<t: print(rdiffsum[t-1] - rdiffsum[s-1])

    else: print(ldiffsum[t-1] - ldiffsum[s-1])


# n,m = list(map(int, input().split()))
# arr = list(map(int, input().split()))
# rdiff = [0]
# for i in range(n-1):
#     a= arr[i]-arr[i+1]
#     if a<0:
#         a=0
#     rdiff.append(a)
    
# ldiff = []
# for i in range(n-1,0,-1):
#     a = arr[i] - arr[i-1]
#     if a<0:
#         a=0
#     ldiff.append(a)
# ldiff.append(0)
# ldiff = ldiff[::-1]
    
# rpre = [0]
# for x in rdiff:
#     rpre.append(rpre[-1] + x)
# lpre = [0]
# for x in ldiff:
#     lpre.append(lpre[-1] + x)
    
# for _ in range(m):
#     s,t = list(map(int, input().split()))
#     ans = 0
#     if s<t:
#         print(rpre[t] - rpre[s])
#     else:
#         print(lpre[s] - lpre[t])