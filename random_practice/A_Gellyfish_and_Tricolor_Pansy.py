cases = int(input())
for _ in range(cases):
    a,b,c,d = list(map(int, input().split()))#kil player first if possible
    print('Flower' if min(a,c)<min(b,d) else 'Gellyfish')