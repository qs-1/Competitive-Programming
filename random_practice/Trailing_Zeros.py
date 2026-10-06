cnt=0
inp=int(input())
n=5
while n<=inp:
	cnt+= inp//n
	n*=5
print(cnt)