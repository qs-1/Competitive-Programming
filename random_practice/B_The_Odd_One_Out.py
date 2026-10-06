from collections import Counter
s = input()
hs = Counter(s)
for k,v in hs.items():
    if hs[k] == 1:
        print(k)
        break