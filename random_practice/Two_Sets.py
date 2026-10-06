n = int(input())

if n<=2:
    print('NO')
    exit()

psum = [0]
for i in range(1,n+1):
    psum.append(psum[-1] + i)
psum = psum[1:]

if psum[-1]%2==1:
    print('NO')
    exit()

arr = []
for i in range(1,n+1):
    arr.append(i)

arr.sort()
s1 = []
s1sum = 0
s2 = []
s2sum = 0

maxhalfsum = psum[-1]//2

for n in arr[::-1]:
    if s1sum+n <= maxhalfsum:
        s1.append(n)
        s1sum += n
    elif s2sum+n <= maxhalfsum:
        s2.append(n)
        s2sum += n
        
print('YES')
print(len(s1))
print(*s1)
print(len(s2))
print(*s2)