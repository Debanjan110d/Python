a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))
a5 = int(input("Enter number 5: "))

print(a1,a2,a3,a4,a5)

if a1>a2 and a1>a3 and a1>a4 and a1>a5:
    print(a1,"is the greatest number")
elif a2>a1 and a2>a3 and a2>a4 and a2>a5:
    print(a2,"is the greatest number")
elif a3>a1 and a3>a2 and a3>a4 and a3>a5:
    print(a3,"is the greatest number")
elif a4>a1 and a4>a2 and a4>a3 and a4>a5:
    print(a4,"is the greatest number")
else:
    print(a5,"is the greatest number")
