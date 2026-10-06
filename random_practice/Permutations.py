n = int(input())
if n == 1:
    print(n)
elif n==2 or n==3:
    print("NO SOLUTION")
else:
    # separate different parities since same
    #  parity wont be consecutive (1 diff) 
    e = 2
    while e<=n:
        print(e,end = ' ')            
        e+=2
    
    o = 1
    while o<=n:
        print(o,end = ' ')            
        o+=2
    