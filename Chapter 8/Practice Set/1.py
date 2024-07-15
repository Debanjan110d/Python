def find_greatest(a, b, c):

    return max(a, b, c)


num1 = 101
num2 = 252
num3 = 183

greatest_num = find_greatest(num1, num2, num3)
print(f"The greatest number  is {greatest_num}.")

#or

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(greatest(10,25,18))
