cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input()

    # infinite minecraft water type shit
    # need a run of ...s then keep moving middle
    # to fill all others
    
    if "..." in s:
        print(2)
    else:
        print(s.count('.'))
            
