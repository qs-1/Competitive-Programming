m = {
    "Ocelot": "1",
    "Serval": "2",
    "Lynx": "3"}

s = input().split()

if m[s[0]] >= m[s[1]]:
    print("Yes")
else:
    print('No')