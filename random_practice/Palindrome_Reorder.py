from collections import Counter
s = input()
hashi = Counter(s)

oddchars = [c for c,v in hashi.items() if v&1 == 1]
if len(oddchars)>1:
    print('NO SOLUTION')
else:
    left = "".join(c*(v//2) for c,v in hashi.items() if v&1 == 0)
    mid = oddchars[0] * hashi[oddchars[0]] if oddchars else ""
    right = left[::-1]
    print(left + mid + right)

# s = input()

# odds = 0
# hashi = {}
# for c in s:
#     if c not in hashi:
#         hashi[c] = 0
#     hashi[c] += 1

#     if hashi[c]&1==1:
#         odds+=1
#     else:
#         odds-=1
    
# if odds>1:
#     print('NO SOLUTION')
# else:
#     ans = []
#     for c in hashi:
#         if hashi[c]&1 == 1:
#             oddchar = c
#             continue
#         for i in range(hashi[c]//2):
#             ans.append(c)

#     for c in ans:
#         print(c,end="")
#     if odds:
#         for i in range(hashi[oddchar]):
#             print(oddchar,end="")
#     for c in ans[::-1]:
#         print(c,end="")