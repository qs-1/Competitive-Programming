arr = []
for __ in range(4):
    arr.append(list(map(int, input().split())))
v=1;prev = sum(arr[0][j] for j in range(4))
for i in range(3):
    x = sum(arr[i][j] for j in range(4)) #sum rows
    if x!=prev:v=0;break
if v:
    for i in range(4):
        x = sum(arr[j][i] for j in range(4)) #sum cols
        if x!=prev:v=0;break
print("magic" if v else 'not magic')
