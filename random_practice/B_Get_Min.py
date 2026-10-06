cases = int(input())
balls = []

for _ in range(cases):
    x = list(map(int, input().split()))
    if len(x) == 1:
        maxx = min(balls)   
        balls.remove(maxx)
        print(maxx)
    else:
        put = x[1]
        balls.append(put)