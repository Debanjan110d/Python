from functools import reduce

l  = [111, 2, 65, 5553, 635, 65, 74, 45,55]

def greater(a,b):
    if (a>b):
        return a
    return b


print(reduce(greater, l))#reduce er fist er ta function then tar por jeta lagbe seta