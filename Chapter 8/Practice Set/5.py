def pattern(a):
    if(a==0):
        return
    pattern(a-1)
    print("*"*a)

pattern(10)