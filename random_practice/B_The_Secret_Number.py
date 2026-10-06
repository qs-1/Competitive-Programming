cases = int(input())
for _ in range(cases):
    n = int(input())

    ans = []
    for i in range(1,18):
        rzeros = 1+(10**i)
        if n%rzeros == 0:
            ans.append(n//rzeros)
        if rzeros>n: break
    anslen = len(ans)
    if anslen==0:
        print(0)
        continue
    print(anslen)
    print(*sorted(ans))

    echo "# grind" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin 
git push -u origin main