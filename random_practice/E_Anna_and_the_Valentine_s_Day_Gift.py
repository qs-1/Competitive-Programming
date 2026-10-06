import sys
input = sys.stdin.readline

cases = int(input())
for _ in range(cases):
    n,m = list(map(int, input().split()))
    arr = list(input().split())

    #anna can only win if she removes enough
    #which makes final digs <= m
    #num itself dosent matter, only its number of digits do

    endzeros = []
    for n in arr:
        endzeros.append(len(n) - len(n.strip('0')))
    endzeros = sorted(endzeros, reverse = True)

    #start with anna, then sasha picks next with most ending 0s and 
    #pairs with another number (like with the new num anna just made without
    #any endin 0s)
    final = sum(len(x) for x in arr)
    final -= sum(endzeros[i] for i in range(0, len(endzeros), 2))

    print('Anna' if final<=m else 'Sasha')